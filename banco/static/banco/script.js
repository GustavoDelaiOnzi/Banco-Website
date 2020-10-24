function debito(){
    document.getElementById("todas-transacoesid").className = "hidden";
    document.getElementById("transacoes-debitoid").className = "todas-transacoes";
    document.getElementById("transacoes-creditoid").className = "hidden";
}
function todas(){
    document.getElementById("todas-transacoesid").className = "todas-transacoes";
    document.getElementById("transacoes-debitoid").className = "hidden";
    document.getElementById("transacoes-creditoid").className = "hidden";
}
function credito(){
    document.getElementById("todas-transacoesid").className = "hidden";
    document.getElementById("transacoes-debitoid").className = "hidden";
    document.getElementById("transacoes-creditoid").className = "todas-transacoes";
}