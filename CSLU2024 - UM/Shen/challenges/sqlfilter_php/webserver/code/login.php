<?php
ini_set('display_errors', 0);

require_once "db.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['password'])) {

        $password = $_POST['password'];

        $blacklist = array("-", "+", "|", "/", "%2F", "%2f", "*", "%2A", "%2a", " ", "%20", "	", "%09", "(", "%28", ")", "%29", "%00", "%0D", "%0d", "%0A", "%0a", "%0B", "%0b", "%0C", "%0c", "%0D", "%0d", "%A0", "%a0"); // Blacklist spaces, no SQLi

        foreach ($blacklist as $char) {
            if ( (strpos($password, $char) !== false) ) {
                http_response_code(400);
                die("Sorry hacker, the password contains a blacklisted character: \"$char\".");
            }
        }
        
        $sql = "SELECT id, username, password FROM users WHERE BINARY username = 'admin' AND password = '$password'";
        $result = mysqli_query($db_connection, $sql);
        if ($result) {
            if (mysqli_num_rows($result) === 1) { //check if the only user successfully logged in
                echo "flag{fake_flag}";
                exit();
            } else {
                echo "Invalid credentials";
                exit(); 
            }
            mysqli_free_result($result);
        } else {
            echo "Error executing query: " . mysqli_error($db_connection);
        }



    }
    
    
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0;
        }

        .container {
            max-width: 300px;
            width: 100%;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }

        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
            box-sizing: border-box; /* Ensure padding and border are included in element's total width */
        }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 3px;
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>

</head>
<body>
    <form action="login.php" method="POST">
        <h1>Admin Login</h1>
        <label for="password">Password:</label>
        <input type="text" id="password" name="password">
        <input type="submit" value="Login">
    </form> 
</body>
</html>