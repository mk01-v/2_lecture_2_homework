Указываем в config.json
{
	"os": {"type":"windows", "version":"8.1"}.
	"browser": {"type":"firefox", "version":"35.0.1"}
}

в CMD
import json
f = open ("C:/Python/config.json")
res = json.load(f)

res ['browser']['firefox']
>>>firefox
f.close()
