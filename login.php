<?php 
//Definir os dados de login(Futuramente será via BD)
$usuario_correto = "admin";
$senha_correta = "123456";

//Dados do formulario
$usuario = $_POST['username'] ??'';
$senha = $_POST['password'] ?? '';

// Verifica se estão corretos
if($usuario === $usuario_correto && $senha === $senha_correta){
    header("localtion: index.html");
    exit;
}else{
    // rereciona de volta com erro
    header("location: login.html?erro=1");
    exit;
}
?>