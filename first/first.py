import subprocess
def plan(AB, BC, CA):
    # Полупериметр
    p = (AB + BC + CA) / 2
    # Площадь по формуле Герона
    S = math.sqrt(p * (p - AB) * (p - BC) * (p - CA))
    # Радиус вписанной окружности: r = S / p
    r = S / p
    # Радиус описанной окружности: R = abc / (4S)
    R = (AB * BC * CA) / (4 * S)
    print(f"Расчёт: r = {r}, R = {R}, S = {S}")
    # Текст программы на Asymptote
    asy_code = f"""
    // Масштаб: одна единица равна 0.7 см
    unitsize(0.7cm);
    // Вершины: B в начале координат, C на оси x,
    // координаты A подобраны для сторон 13, 14, 15
    pair B=(0,0), C=({BC},0), A=(5,12);
    // Длины сторон
    real a=length(B-C), b=length(C-A), c=length(A-B);
    // Полупериметр и площадь (через векторное произведение)
    real p=(a+b+c)/2, S_val=abs(cross(B-A,C-A))/2;
    // Радиусы вписанной и описанной окружностей
    real r=S_val/p, R=a*b*c/(4*S_val);
    // Центр вписанной окружности I (точка пересечения биссектрис)
    pair I=(a*A+b*B+c*C)/(a+b+c);
    // Вспомогательная величина для центра описанной окружности
    real d=2*(A.x*(B.y-C.y)+B.x*(C.y-A.y)+C.x*(A.y-B.y));
    // Центр описанной окружности O по координатам вершин
    pair O=((abs(A)^2*(B.y-C.y)+abs(B)^2*(C.y-A.y)+abs(C)^2*(A.y-B.y))/d,
            (abs(A)^2*(C.x-B.x)+abs(B)^2*(A.x-C.x)+abs(C)^2*(B.x-A.x))/d);
    write("r = ", r); write("R = ", R);
    // Треугольник ABC
    draw(A--B--C--cycle, black+1.2);
    // Вписанная (синяя) и описанная (красная) окружности;
    // D - точка касания вписанной окружности со стороной BC
    draw(circle(I,r), blue); draw(circle(O,R), red+dashed); pair D=(I.x,0);
    // Радиус r (синий) и радиус R (красный пунктир)
    draw(I--D, blue);  draw(O--A, red+dashed);
    // Отмечаем точки
    dot(A); dot(B); dot(C); dot(I); dot(O); dot(D);
    // Подписи вершин, центров и радиусов
    label("$A$",A,N);  label("$B$",B,SW);  label("$C$",C,SE);
    label("$I$",I,NE); label("$O$",O,NE);  label("$D$",D,S);
    label("$r$",(I+D)/2,E,blue);  label("$R$",(O+A)/2,W,red);
    """
    # Сохраняем код чертежа в файл plan.asy
    with open("plan.asy", "w", encoding="utf-8") as f:
        f.write(asy_code)
    # Компилируем чертёж в PDF программой asy
    subprocess.run(["asy", "-f", "pdf", "plan.asy"])
    # Открываем получившийся PDF
    subprocess.run(["xdg-open", "plan.pdf"])
# Запуск для треугольника со сторонами 13, 14, 15
plan(13, 14, 15)
