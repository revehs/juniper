<html>
        <head>
        </head>
        <body>
                <?php
                $file = '/home/hans/git/juniper/juniper/manual_file.set';
		$nn = $_REQUEST['config'];
		file_put_contents($file, $nn); 
		
		$command = "/home/hans/git/juniper/juniper/manual_module.py";
                $result = shell_exec($command);
                echo "<pre>$result</pre>";
                ?>
		<br>
		<li>Success</li>
        </body>
</html>
