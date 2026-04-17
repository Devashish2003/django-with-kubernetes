from django.http import HttpResponse

from django.http import HttpResponse

def start(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Kubernetes chalja bhai</title>
      <style>
        body {
          background-color: #121212;
          color: #00FF99;
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
          margin: 0;
        }
        h1 {
          font-size: 3rem;
          animation: pulse 1s infinite alternate;
        }

        @keyframes pulse {
          from {
            transform: scale(1);
            opacity: 0.8;
          }
          to {
            transform: scale(1.05);
            opacity: 1;
          }
        }
      </style>
    </head>
    <body>
      <h1>Kubernetes chal gaya 😎</h1>
    </body>
    </html>
    """)
