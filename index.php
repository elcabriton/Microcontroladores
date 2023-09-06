<?php


$user = 'root';
$servername='127.0.0.1:4444';
$pass='';
$conn = new mysqli($servername, $user, $pass);
?>






<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilo.css">
    <link rel="stylesheet" type="html5" href="historico.html">
    <link rel="stylesheet" type="html5" href="senha.html">
    <title>TRANCA ELETRÔNICA</title>
</head>
<body> 
    <h1>TRANCA ELETRÔNICA</h1>
    <div class="principal">
        <div class="pag">
            <div class="nav"> 
                <div class="nav-item">
                    <button type="submit" class="button">
                        <a href="historico.php" class="button">
                            <p>HISTÓRICO</p>
                        </a>
                    </button>
                </div>
                <div class="nav-item">
                    <button type="submit" class="button">    
                        <a href="senha.php" class="button">
                            <P>SENHA</P>
                        </a>
                    </button>
                </div>
                <div class="nav-item">
                    <button type="submit" class="button">
                        <i>ABRIR</i>  
                    </button>  
                </div>
            </div>
        </div>
    </div>
</body>
</html>
