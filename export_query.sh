sqlite3 db/relevation.db "select judgementapp_query.qId, judgementapp_query.category['1'], judgementapp_query.comment from judgementapp_query" | sed "s/|/ /g" | sed -E "s/^([0-9]+) /\1 0 corpus\//g"
