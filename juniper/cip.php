<html>
        <head>
        </head>
        <body>
                <?php
                $file = '/home/hans/git/juniper/juniper/cip_file.set';
		$nn = $_REQUEST['email'];
		file_put_contents($file, $nn); 
		
		$command = "/home/hans/git/juniper/juniper/cip_module.py";
                $result = shell_exec($command);
                echo "<pre>$result</pre>";
                ?> 
		<br>
		<li>Success</li>
        </body>
</html>
