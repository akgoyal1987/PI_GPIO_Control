<html>
	<head>
		<title>First PHP Page in Raspberry Pi</title>	
	</head>
	<body>
		<?php
			echo exec("sudo python low.py ".$_GET['pin']);

		?>
	</body>
</html>