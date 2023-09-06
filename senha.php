




<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilo.css">
    <title>SENHA</title>
</head>
<body>
    <form method="post" action="">
    <h1 class="center">SENHA</h1>
    <div class="principal">
        <div class="pag2">
            <div class="nav"> 
                       <div class="input ">
                        <div class="linhas ">
                            <input type="password" name="senha" placeholder="Senha da tranca" class="linhas">
                        </div> 
                        <div class="linhas">
                            <input type="password" name="NovaSenha" value="" placeholder="Nova Senha" class="linhas">
                        </div>
                        <div class="linhas">
                            <input type="password" name="confirmaS" value="" placeholder="Confirma senha" class="linhas">
                        </div>

                        <p>
 

                        <button type="submit" class="button"name="enviar">
                            <span>Enviar</span>
                        </div>
            </div>
        </div>
    </div>
    <?php
    if(isset($_POST['enviar'])){
        backend();
    }
  
    ?>
</form>


</body>
</html>

<?php

function backend(){
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
         $ultimaSenha=$row["senha"];
        
    }
} 
else {
    echo "0 results";
}











    $novaSenha= $_POST['NovaSenha'];
    $senha= $_POST['senha'];
    date_default_timezone_set('America/Sao_Paulo');
    $data= date('Y-m-d H:i:s');
    $confirmaS= $_POST['confirmaS'];
    

    // SQL
$SQL= "insert into password_access (senha,ultimo_acesso,fotos_tentativas) values ('{$novaSenha}', '{$data}', 'null')";
if($ultimaSenha==$senha){
    if($confirmaS==$novaSenha){
  
        $conn->query($SQL);
        echo "Senha alterada com sucesso";
      }
      else{
          echo "Senhas não conferem";
      }
    
}
else{
    echo "Senha incorreta";
}

    }
        ?>
