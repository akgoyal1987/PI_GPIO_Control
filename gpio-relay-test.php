<html>
	<head>
		<title>First PHP Page in Raspberry Pi</title>	
	</head>
	<body>
		<?php
			echo exec("sudo python gpio-relay-test.py");
		?>
	</body>
</html>