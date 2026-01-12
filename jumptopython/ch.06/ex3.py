# 게시판 페이징

def get_total_page(m,n):
    if m % n == 0:
        return m // n
    else:
        return (m // n) + 1  

print(get_total_page(5, 10)) 
print(get_total_page(10, 10))  
print(get_total_page(15, 10))  