data = 'minhnhutvh@gmail.com Sat Jan 5 09:14:16'
start_position = data.find("@")
end_position = data.find(" ", start_position)
host = data[start_position+1:end_position]
print(host)
