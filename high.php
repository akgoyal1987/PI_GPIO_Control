<html>
	<head>
		<title>First PHP Page in Raspberry Pi</title>	
	</head>
	<body>
		<?php
			echo exec("sudo python high.py ".$_GET['pin']);

		?>
	</body>
</html>