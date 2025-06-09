# 📚 Study Tracker

A comprehensive web application for tracking study time, managing subjects, and analyzing productivity with a minimizable Pomodoro timer and real-time synchronization across devices.

## 🎯 Project Overview

Study Tracker is a full-stack web application designed to help students and professionals monitor their study habits, organize subjects hierarchically, and boost productivity through integrated Pomodoro timer functionality. The application features a unique minimizable timer widget that continues tracking time even when collapsed to a floating interface.

### ✨ Key Features

- **🍅 Minimizable Pomodoro Timer**: Floating widget that tracks study time without interrupting workflow
- **📊 Real-time Analytics**: Visual charts and heatmaps showing daily, weekly, and monthly progress
- **📁 Hierarchical Subject Management**: Organize subjects with parent-child relationships
- **📝 Task Management**: Estimate time, track completion, and manage study tasks
- **🔄 Cross-device Synchronization**: Access your data from any device with Firebase integration
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **🎨 Aesthetic Interface**: Clean, modern UI with customizable themes

## 🛠️ Tech Stack

### Backend
- **FastAPI** (Python 3.11+) - High-performance web framework
- **Firebase Admin SDK** - Authentication and cloud database
- **WebSockets** - Real-time timer updates
- **Uvicorn** - ASGI server for production deployment

### Frontend
- **React 18** - Modern JavaScript framework
- **Vite** - Fast build tool and development server
- **Axios** - HTTP client for API communication
- **CSS3** - Custom styling with animations

### Database & Authentication
- **Firebase Firestore** - NoSQL cloud database
- **Firebase Authentication** - Secure user management

### Analytics & Visualization
- **Matplotlib** - Python plotting library
- **Seaborn** - Statistical data visualization
- **Pandas** - Data analysis and manipulation
- **NumPy** - Numerical computing

### Installation

1. **Clone the repository**
- git clone https://github.com/siddhamapple/study-tracker.git
- cd study-tracker

2. **Set up Firebase**
- Create a Firebase project at https://console.firebase.google.com
- Enable Firestore Database and Authentication
- Download `serviceAccountKey.json` and place it in `backend/`

3. **Backend Setup**
- cd backend
- pip install -r requirements.txt

4. **Frontend Setup**
- cd frontend
- npm install

### Running the Application

#### Development Mode

1. **Start Backend Server**
- cd backend
- uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

2. **Start Frontend Development Server**
-cd frontend
-npm run dev

3. **Access the Application**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

#### Production Mode

1. **Build Frontend**
- cd frontend
- npm run build
- cp -r dist/assets/* ../backend/static/
- cp dist/index.html ../backend/templates/


2. **Run Production Server**
- cd backend
- uvicorn app.main:app --host 0.0.0.0 --port 8000


## 🎮 Usage

### Starting a Study Session

1. **Open the application** in your browser
2. **Click the timer widget** to expand the Pomodoro interface
3. **Select a subject** from your organized list
4. **Click "Start"** to begin your study session
5. **Minimize the timer** using the ➖ button to continue working

### Managing Subjects

- **Create subjects** with custom colors and hierarchical organization
- **Edit subject details** including names and parent relationships
- **View subject-specific analytics** and time tracking

### Viewing Analytics

- **Daily Reports**: See today's study time breakdown
- **Weekly Progress**: Track consistency and patterns
- **Productivity Heatmap**: Visualize long-term study habits
- **Subject Comparison**: Compare time spent across different topics

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the backend directory:
FIREBASE_CREDENTIALS_PATH=serviceAccountKey.json
CORS_ORIGINS=["http://localhost:3000", "http://localhost:5173"]


### Firebase Setup

1. **Authentication**: Enable Email/Password and Google sign-in
2. **Firestore Rules**: Configure security rules for user data isolation

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for JavaScript/React code
- Write descriptive commit messages
- Include tests for new features
- Update documentation as needed

## 📊 API Documentation

The API provides RESTful endpoints for:

- **Authentication**: User login and registration
- **Subjects**: CRUD operations for subject management
- **Sessions**: Study session tracking and retrieval
- **Tasks**: Task management and completion tracking
- **Analytics**: Data aggregation and reporting


## 🐛 Known Issues

- Timer synchronization may lag on slow network connections
- Mobile timer widget positioning needs refinement

## 🔮 Future Enhancements

- [ ] Mobile app development (React Native)
- [ ] Collaborative study rooms
- [ ] Integration with calendar applications
- [ ] Advanced AI-powered study recommendations
- [ ] Offline mode support
- [ ] Export data to CSV/PDF formats


## 🙏 Acknowledgments

- **Firebase** for providing free backend infrastructure
- **React community** for excellent documentation and resources
- **FastAPI** for the intuitive Python web framework
- **Pomodoro Technique** creators for the productivity methodology
- **Google** - Devta :happy

## 📞 Support

If you encounter any issues or have questions:
- Email: siddhamjainn@gmail.com
- whatsapp: +919625208689

## 📈 Project Status

**Current Version**: 1.0.0  
**Status**: Active Development  


**Happy Studying! 🎓**

Made with ❤️ for productive learners and for myself especially.

