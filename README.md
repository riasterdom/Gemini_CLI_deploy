# Gemini_CLI_deploy

A simple Streamlit mini-game: **Rock, Paper, Scissors**  
Deployable to Google Cloud Run.

## Game Features

- Play Rock, Paper, Scissors against the computer.
- Interactive UI with buttons for each choice.
- Instant feedback on your selection and the computer's move.
- Game logic and results displayed clearly.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/riasterdom/Gemini_CLI_deploy.git
   cd Gemini_CLI_deploy
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app:**
   ```bash
   streamlit run app.py
   ```

## Deploying to Google Cloud Run

1. **Containerize the app**  
   (See [Streamlit docs](https://docs.streamlit.io/streamlit-cloud/deploy/docker) for Docker setup)

2. **Build and push the container:**
   ```bash
   gcloud builds submit --tag gcr.io/<PROJECT-ID>/gemini-cli-deploy
   ```

3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy gemini-cli-deploy \
     --image gcr.io/<PROJECT-ID>/gemini-cli-deploy \
     --platform managed \
     --region <YOUR-REGION> \
     --allow-unauthenticated
   ```

4. **Access your app:**  
   Cloud Run will provide a public URL after deployment.

## File Structure

```
.
├── app.py            # Streamlit app source code
├── README.md         # Project documentation
├── requirements.txt  # Python dependencies
└── Dockerfile        # For containerization
```

## About

This project demonstrates a basic interactive game using Streamlit, ready for deployment on Google Cloud Run.  
Modify or extend the game logic in `app.py` for more features!
