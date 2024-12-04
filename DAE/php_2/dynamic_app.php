<?php
// Define and use a named constant
define("DB_HOST", "localhost");
define("DB_USER", "root");
define("DB_PASSWORD", "");
define("DB_NAME", "example_database");

// Establish a connection to the MySQL database
$connection = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

// Check connection
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}
echo "Connected successfully.<br>";

// Function to modularize code
function fetchUserData($connection, $userID) {
    $stmt = $connection->prepare("SELECT * FROM users WHERE id = ?");
    $stmt->bind_param("i", $userID);
    $stmt->execute();
    $result = $stmt->get_result();
    $data = $result->fetch_assoc();
    $stmt->close();
    return $data;
}

// Create an associative array
$user = fetchUserData($connection, 1);
echo "User Info: <br>";
print_r($user);

// Control flow using IF-ELSE
if ($user) {
    echo "<br>User found: " . $user['name'];
} else {
    echo "<br>No user found with the given ID.";
}

// Automate repetitive tasks using a loop
echo "<br><br>List of users:<br>";
$query = "SELECT * FROM users";
$result = $connection->query($query);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "ID: " . $row['id'] . " - Name: " . $row['name'] . "<br>";
    }
} else {
    echo "No users found.<br>";
}

// Create and manipulate collection data
$associativeArray = ["name" => "John Doe", "email" => "john@example.com"];
$multiDimensionalArray = [
    ["id" => 1, "name" => "Alice"],
    ["id" => 2, "name" => "Bob"]
];

echo "<br>Associative Array:<br>";
foreach ($associativeArray as $key => $value) {
    echo "$key: $value<br>";
}

echo "<br>Multi-dimensional Array:<br>";
foreach ($multiDimensionalArray as $item) {
    foreach ($item as $key => $value) {
        echo "$key: $value<br>";
    }
    echo "<br>";
}

// Close the database connection
$connection->close();
?>