<html>
        <head>
	        <style type="text/css">
	            header {
	                border-bottom: 5px solid green;
	                padding: 10px 40px;
	                }
	            h1 {
	                font-size: 1.4em;
	           		 }
	        </style>
        </head>
        
        
        
        <body>
        
        <header>
        <h1>CIP Automation</h1>
        V1.11
        </header>
                <?php
                $file = '/home/hans/git/juniper/juniper/manual_file.set';
		$nn = $_REQUEST['config'];
		file_put_contents($file, $nn); 
		
		$command = "/home/hans/git/juniper/juniper/manual_module.py";
                $result = shell_exec($command);
                echo "<pre>$result</pre>";
                ?>
		<br>
	
        </body>
</html>
