# Import protobuf fix first
import protobuf_fix

from flask import Flask, render_template, jsonify, request
import threading
import time
import logging
from app import FF_CLIENT, restart_program
import os

app = Flask(__name__)

# Global variables to track bot status
bot_status = {
    "running": False,
    "connected": False,
    "last_activity": None,
    "error": None
}

bot_thread = None
client_instance = None

def run_bot():
    """Run the bot in a separate thread"""
    global bot_status, client_instance
    
    try:
        bot_status["running"] = True
        bot_status["error"] = None
        bot_status["last_activity"] = time.time()
        
        # Initialize the client with credentials from environment or default
        uid = os.getenv('FF_UID', '4207697700')
        password = os.getenv('FF_PASSWORD', 'E71FE984531619DC92F7539E95337690A3A8FF8D5055820C01F9A363F22B0489')
        
        client_instance = FF_CLIENT(uid=uid, password=password)
        client_instance.start()
        
        bot_status["connected"] = True
        bot_status["last_activity"] = time.time()
        
    except Exception as e:
        bot_status["error"] = str(e)
        bot_status["running"] = False
        bot_status["connected"] = False
        logging.error(f"Bot error: {e}")

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html', status=bot_status)

@app.route('/api/status')
def get_status():
    """API endpoint to get bot status"""
    return jsonify(bot_status)

@app.route('/api/start', methods=['POST'])
def start_bot():
    """Start the bot"""
    global bot_thread, bot_status
    
    if bot_status["running"]:
        return jsonify({"success": False, "message": "Bot is already running"})
    
    try:
        bot_thread = threading.Thread(target=run_bot)
        bot_thread.daemon = True
        bot_thread.start()
        
        return jsonify({"success": True, "message": "Bot started successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Failed to start bot: {str(e)}"})

@app.route('/api/stop', methods=['POST'])
def stop_bot():
    """Stop the bot"""
    global bot_status
    
    bot_status["running"] = False
    bot_status["connected"] = False
    bot_status["last_activity"] = None
    
    return jsonify({"success": True, "message": "Bot stopped"})

@app.route('/api/restart', methods=['POST'])
def restart_bot():
    """Restart the bot"""
    global bot_thread, bot_status
    
    # Stop current bot
    bot_status["running"] = False
    bot_status["connected"] = False
    
    # Wait a moment
    time.sleep(2)
    
    # Start new bot thread
    try:
        bot_thread = threading.Thread(target=run_bot)
        bot_thread.daemon = True
        bot_thread.start()
        
        return jsonify({"success": True, "message": "Bot restarted successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Failed to restart bot: {str(e)}"})

@app.route('/health')
def health_check():
    """Health check endpoint for Render"""
    return jsonify({"status": "healthy", "bot_running": bot_status["running"]})

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Get port from environment variable (Render requirement)
    port = int(os.getenv('PORT', 5000))
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=port, debug=False)
