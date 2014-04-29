<html>
        <head>
        </head>
        <body>
                <?php
                $file = '/home/hans/git/juniper/juniper/config.set';
		$nn = $_REQUEST['config'];
		file_put_contents($file, $nn); 
		
		$command = "/home/hans/git/juniper/juniper/module_cli.py";
                $result = shell_exec($command);
                echo "<pre>$result</pre>";
                ?>
		<br>
		<li>Success</li>
        </body>
</html>
