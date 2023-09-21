<!DOCTYPE html>
<html>
<head>
    <title>ProjectMystic</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
        }

        .container {
            padding: 50px;
        }

        .message {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to ProjectMystic</h1>
        <p>Uncover the mysteries of the digital realm.</p>
        <div class="message">
            <?php
                // Generate a random mysterious message
                $mysteriousMessages = [
                    "Unlock the secrets of the code.",
                    "Embrace the unknown.",
                    "In the world of bytes, find your magic.",
                    "The source code holds hidden knowledge.",
                    "ProjectMystic: Where coding meets mystery."
                ];

                $randomMessage = $mysteriousMessages[array_rand($mysteriousMessages)];
                echo $randomMessage;
            ?>
        </div>
    </div>
</body>
</html>
