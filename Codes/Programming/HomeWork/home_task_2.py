function = int(input("Введите номер решаемого задания [1, 2]: "))

if function == 1:
    blocked_ip_list = {'192.168.1.1', '192.168.1.2', '192.168.4.3', 
                '192.234.2.6', '192.225.3.7', '192.456.9.1',
                '168.192.4.5', '192.162.2.6', '186.186.1.1', 
                '168.192.10.15', '192.119.22.16', '192.119.1.1', 
                '192.192.4.5', '192.192.10.10', '192.119.1.5'}

    def blocked_ip(ip_adress):
        ip_adress = ip_adress.replace(' ', '')  # Удаляем пробелы
        if ip_adress in blocked_ip_list:
            return True
        else:
            return False
    
    print("IP-адрес должен быть следующих видов:" + "\n" 
          + "\033[36mXXX.XXX.X.X \033[0m" + '\n'
          + "\033[36mXXX.XXX.XX.X \033[0m" + '\n'
          + "\033[36mXXX.XXX.XXX.X \033[0m") 
    inputed_ip = input("Введте IP-адрес устройства: ")
    inputed_ip = inputed_ip.replace(' ', '')
    
    if blocked_ip(inputed_ip):
        print("\033[31mДоступ с IP-адреса {} запрещён!\033[0m".format(inputed_ip))
    else:
        print("\033[32mДоступ с IP-адреса {} разрешён!\033[0m".format(inputed_ip))

if function == 2:
    import re

    blocked_ip_list = {'192.168.1.1', '192.168.1.2', '192.168.4.3', 
                '192.234.2.6', '192.225.3.7', '192.456.9.1',
                '168.192.4.5', '192.162.2.6', '186.186.1.1', 
                '168.192.10.15', '192.119.22.16', '192.119.1.1', 
                '192.192.4.5', '192.192.10.10', '192.119.1.5'}
    
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,2}$'
    print("IP-адрес должен быть следующих видов:" + "\n" 
          + "\033[36mXXX.XXX.X.X \033[0m" + '\n'
          + "\033[36mXXX.XXX.XX.X \033[0m" + '\n'
          + "\033[36mXXX.XXX.XXX.X \033[0m") 

    def blocked_ip(ip_adress):
        if ip_adress in blocked_ip_list:
            return True
        else:
            return False

    while True:
        inputed_ip = input("Введте IP-адрес устройства: ")
        if re.match(ip_pattern, inputed_ip):
            if blocked_ip(inputed_ip):
                print("\033[31mДоступ с IP-адреса {} запрещён!\033[0m".format(inputed_ip))
            else:
                print("\033[32mДоступ с IP-адреса {} разрешён!\033[0m".format(inputed_ip))
                break
        else:
            print("\033[31mВы ввели некорректный IP-адрес!\033[0m".format(inputed_ip))
            print("\033[31mПопробуйте ещё раз\033[0m")