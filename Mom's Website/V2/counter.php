<?php
// Path to the text file where the hit count is stored
$counter_file = 'counter.txt';

// Check if the file exists
if (!file_exists($counter_file)) {
    // Create the file and set the count to 0 if it doesn't exist
    file_put_contents($counter_file, '0');
}

// Read the current count
$count = (int)file_get_contents($counter_file);

// Increment the count
$count++;

// Write the new count back to the file
file_put_contents($counter_file, (string)$count);

// Return the new count as JSON for the frontend
echo json_encode(['count' => $count]);
?>
