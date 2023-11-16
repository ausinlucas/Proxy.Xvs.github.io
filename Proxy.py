from flask import Flask, render_template_string, request, redirect, url_for
import webbrowser

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proxy_Xvs</title>
    <style>
        body {
            background-color: #000; /* Black background */
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden; /* Hide overflow to prevent scrollbars */
        }

        .content {
            text-align: center;
            position: relative; /* Set position to relative for absolute positioning of dots */
        }

        #typing-text {
            display: inline-block;
            animation: colorAnimation 5s infinite alternate;
            color: #ff69b4; /* Initial pink color */
            text-shadow: 0 0 5px #ff69b4; /* Add a subtle shadow for effect */
        }

        /* Hide the cursor animation on focus for the input element */
        input:focus {
            outline: none;
        }

        /* Dots floating around */
        .dot {
            position: absolute;
            background-color: #fff; /* White dots */
            width: 8px;
            height: 8px;
            border-radius: 50%;
            animation: floatAnimation 3s infinite linear;
        }

        @keyframes floatAnimation {
            0% {
                transform: translate(0, 0);
            }
            50% {
                transform: translate(50px, -50px);
            }
            100% {
                transform: translate(0, 0);
            }
        }

        /* Responsive iframe */
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        /* Expand/Minimize button */
        #expand-button {
            background-color: #ff69b4;
            color: #fff;
            padding: 8px 16px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
        }

        /* Fast link */
        #fast-link {
            color: #ff69b4;
            text-decoration: none;
            padding: 8px 16px;
            cursor: pointer;
            border: 1px solid #ff69b4;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1 id="typing-text"></h1>
        <form id="search-form">
            <label for="query">Search:</label>
            <input type="text" id="query" name="query" required>
            <input type="submit" value="Search">
        </form>
        <a id="fast-link" href="www.ubg365.github.io" target="iframe-container">Drag and Drop Me!</a>
        <button id="expand-button" onclick="toggleFullscreen()">Expand</button>
        <div id="iframe-container"></div>
    </div>

    <!-- Dots floating around -->
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            var body = document.body;

            // Create dots and append them to the body
            for (var i = 0; i < 50; i++) {
                var dot = document.createElement('div');
                dot.className = 'dot';
                dot.style.top = Math.random() * window.innerHeight + 'px';
                dot.style.left = Math.random() * window.innerWidth + 'px';
                body.appendChild(dot);
            }

            // Handle form submission
            var searchForm = document.getElementById('search-form');
            var iframeContainer = document.getElementById('iframe-container');

            searchForm.addEventListener('submit', function (event) {
                event.preventDefault();

                // Get the search query
                var queryInput = document.getElementById('query');
                var query = queryInput.value;

                // Create and set the iframe source only if the search bar is not empty
                if (query.trim() !== '') {
                    var iframe = document.createElement('iframe');
                    iframe.src = 'https://' + query;
                    iframeContainer.innerHTML = '';
                    iframeContainer.appendChild(iframe);
                }
            });
        });

        // Function to toggle fullscreen
        function toggleFullscreen() {
            var iframe = document.querySelector('iframe');

            if (iframe) {
                if (!document.fullscreenElement) {
                    iframe.requestFullscreen().then(() => {
                        document.getElementById('expand-button').textContent = 'Minimize';
                    });
                } else {
                    document.exitFullscreen().then(() => {
                        document.getElementById('expand-button').textContent = 'Expand';
                    });
                }
            }
        }
    </script>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // Text for the typing animation
            var textToType = 'Proxy_Xvs';

            // Get the typing-text element
            var typingTextElement = document.getElementById('typing-text');

            // Function to perform the typing animation
            function typeText(index) {
                typingTextElement.textContent = textToType.substring(0, index);
                if (index < textToType.length) {
                    setTimeout(function () {
                        typeText(index + 1);
                    }, 100); // Adjust the typing speed here (milliseconds)
                }
            }

            // Start the typing animation when the page loads
            typeText(0);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def hello_world():
    return render_template_string(html_template)

if __name__ == '__main__':
    # Open the web browser when the application starts
    webbrowser.open_new('http://127.0.0.1:5000/')
    # Run the Flask application in debug mode
    app.run(debug=True)
