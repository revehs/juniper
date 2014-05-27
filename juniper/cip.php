<html>
        <head>
         <meta charset="utf-8" />
        
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
                $file = '/home/hans/git/juniper/juniper/cip_file.set';
				$nn = $_REQUEST['email'];
				file_put_contents($file, $nn); 
	
		
				$command = "/home/hans/git/juniper/juniper/cip_module.py";
                $result = shell_exec($command);
                echo "<pre>$result</pre>";
                ?> 
		<br>
		
		
				        <form action="./cip_rollback.php" method="POST">
                           		  <p>
                   			      <input type="submit" value="rollback (컨피그 복원)"/>
                         		  </p>
                                      	 </form>
		
		                         <form action="./cip_commit.php" method="POST">
                                          <p>
                                              <input type="submit" value="commit (컨피그 적용)"/>
                                          </p>
                                         </form>  
		
        </body>
</html>
