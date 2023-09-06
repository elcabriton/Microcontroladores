<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilo.css">
    <title>HISTÓRICO</title>
</head>
<body>
    <h1 class="center">HISTÓRICO</h1>
    <div class="pag3">
       
    <div class="his">
            <h3>FOTO</h3>
        <?php
           
            $SQL="select * from password_access";
            $user = 'root';
            $servername='127.0.0.1:4444';
            $pass='';
            $DB='Tranca';
            $conn = new mysqli($servername, $user, $pass,$DB);
            $result = $conn->query($SQL);
            if ($result->num_rows > 0) 
            {
                while($row = $result->fetch_assoc()) {
                
                    ?>
                    <img src="data:image/jpeg;base64,<?php echo base64_encode($row['fotos_tentativas']); ?>" width="100" height="100" />
                   
                  
        <?php
               } 
            }
           
           ?>
        </div>
        <div class="his">
        <h3>DATA/HORA</h3>
        <?php
        $user = 'root';
        $servername='127.0.0.1:4444';
        $pass='';
        $DB='Tranca';
        $conn = new mysqli($servername, $user, $pass,$DB);
        $SQL="select * from password_access";
        $result = $conn->query($SQL);
        if ($result->num_rows > 0) {
            // output data of each row
            while($row = $result->fetch_assoc()) {
                
                 ?>
                 
                 <p><?php
                    echo $row["ultimo_acesso"]                    
                 ?></p>

                 <?php
            }
        } 
        ?>
        
        
            
        
        </div>
    </div>
</body>
</html>