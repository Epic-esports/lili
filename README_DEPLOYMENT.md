# Free Fire Bot - Render.com Deployment Guide

This guide will help you deploy your Free Fire Bot to Render.com as a web service.

## 🚀 Quick Deployment

### Method 1: Using Render Dashboard (Recommended)

1. **Fork/Clone this repository** to your GitHub account
2. **Go to [Render.com](https://render.com)** and sign up/login
3. **Click "New +"** → **"Web Service"**
4. **Connect your GitHub repository**
5. **Configure the service:**
   - **Name**: `free-fire-bot` (or any name you prefer)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python web_app.py`
   - **Plan**: Free (or upgrade if needed)

6. **Set Environment Variables:**
   - `FF_UID`: Your Free Fire UID
   - `FF_PASSWORD`: Your Free Fire password hash
   - `PYTHON_VERSION`: `3.9.0`

7. **Click "Create Web Service"**

### Method 2: Using render.yaml (Automatic)

If you have a `render.yaml` file in your repository (which we've created), Render will automatically detect it and use those settings.

## 📁 Project Structure

```
BOT-main/
├── app.py                 # Original bot logic
├── web_app.py            # Flask web application wrapper
├── templates/
│   └── index.html        # Web dashboard
├── requirements.txt      # Python dependencies
├── render.yaml          # Render configuration
├── Procfile             # Alternative deployment config
├── env.example          # Environment variables template
└── README_DEPLOYMENT.md # This file
```

## 🔧 Configuration

### Environment Variables

Set these in your Render dashboard under "Environment":

- `FF_UID`: Your Free Fire account UID
- `FF_PASSWORD`: Your Free Fire account password hash
- `PORT`: Port number (Render sets this automatically)
- `LOG_LEVEL`: Logging level (optional, default: INFO)

### Web Dashboard Features

Once deployed, you'll have access to:

- **Real-time bot status monitoring**
- **Start/Stop/Restart bot controls**
- **Connection status tracking**
- **Error logging and display**
- **Responsive web interface**

## 🌐 Accessing Your Bot

After deployment, Render will provide you with a URL like:
`https://your-app-name.onrender.com`

## 📱 Web Dashboard Usage

1. **Open your deployed URL**
2. **View bot status** in real-time
3. **Start the bot** using the "Start Bot" button
4. **Monitor connection** status
5. **Stop/Restart** as needed
6. **View error messages** if any occur

## 🔍 Troubleshooting

### Common Issues:

1. **Bot won't start:**
   - Check environment variables are set correctly
   - Verify FF_UID and FF_PASSWORD are valid
   - Check Render logs for error messages

2. **Connection issues:**
   - Ensure your Free Fire credentials are correct
   - Check if the game servers are accessible
   - Verify network connectivity

3. **Deployment fails:**
   - Check that all dependencies are in requirements.txt
   - Verify Python version compatibility
   - Check build logs in Render dashboard

### Logs and Monitoring:

- **Render Dashboard**: View deployment and runtime logs
- **Web Interface**: Real-time status and error messages
- **Health Check**: Visit `/health` endpoint for service status

## 🔒 Security Notes

- **Never commit real credentials** to your repository
- **Use environment variables** for sensitive data
- **Consider using Render's secret management** for production
- **Regularly update dependencies** for security patches

## 📈 Scaling

- **Free Plan**: Limited to 750 hours/month
- **Paid Plans**: Unlimited usage, better performance
- **Auto-scaling**: Available on paid plans

## 🆘 Support

If you encounter issues:

1. **Check Render logs** in the dashboard
2. **Verify environment variables**
3. **Test locally** using `python web_app.py`
4. **Check Free Fire server status**
5. **Review this documentation**

## 🎯 Next Steps

After successful deployment:

1. **Test the web interface**
2. **Configure your Free Fire credentials**
3. **Monitor bot performance**
4. **Set up monitoring/alerts** if needed
5. **Consider upgrading** to a paid plan for better reliability

---

**Happy Botting! 🎮**
