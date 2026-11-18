# a - сторона основания, h - высота
function pyramid(a::Real, h::Real)
    # OM - половина стороны основания
    om = a / 2
    # Апофема SM по теореме Пифагора
    sm = sqrt(h^2 + om^2)
    # Объём: V = (1/3) * S_осн * h
    volume = (1 / 3) * (a^2) * h
    # Площадь основания
    s_base = a^2
    # Площадь боковой поверхности: 4 треугольника с основанием a и высотой SM
    s_side = 4 * (0.5 * a * sm)
    # Площадь полной поверхности
    s_full = s_base + s_side
    # Выводим результаты
    println("Апофема SM = $sm")
    println("Объём V = $volume")
    println("Площадь полной поверхности S_полн = $s_full")
    # Текст программы на Asymptote (значения a и h подставляются из расчетов Julia)
    asy_code = """
    // Масштаб: одна единица равна 1 см
    unitsize(1cm);
    real a=$a, h=$h;
    // Вершины основания ABCD (наклонная проекция квадрата)
    pair A=(0,0), B=(a,0), C=(a+2.4,2), D=(2.4,2);
    // O - центр основания, S - вершина пирамиды, M - середина AB
    pair O=(A+C)/2, S=O+(0,h), M=(A+B)/2;
    // Видимые рёбра (сплошные линии)
    draw(A--B--C, black+1.2);
    draw(S--A, black+1.2); draw(S--B, black+1.2); draw(S--C, black+1.2);
    // Невидимые рёбра (пунктир)
    draw(A--D--C, dashed); draw(S--D, dashed);
    // Высота SO, отрезок OM и апофема SM
    draw(S--O, blue+dashed); draw(O--M, blue+dashed); draw(S--M, red+1.2);
    // Дуга, отмечающая угол phi между апофемой SM и плоскостью основания
    draw(arc(M,0.8,degrees(O-M),degrees(S-M)), red);
    // Отмечаем точки
    dot(S); dot(A); dot(B); dot(C); dot(D); dot(O); dot(M);
    // Подписи вершин и точек
    label("\$S\$",S,N);  label("\$A\$",A,SW); label("\$B\$",B,SE); label("\$C\$",C,E);
    label("\$D\$",D,NW); label("\$O\$",O,SE); label("\$M\$",M,S);
    // Подпись угла
    label("\$\\varphi\$",M+(0.7,0.4),red);
    // Подписи высоты h и стороны основания a
    label("\$h=$h\$",(O+S)/2,E,blue);  label("\$a=$a\$",(A+B)/2+(0,-0.6));
    """
    # Сохраняем код чертежа в файл pyramid.asy
    open("pyramid.asy", "w") do f
        write(f, asy_code)
    end
    # Компилируем чертёж в PDF программой asy
    run(`asy -f pdf pyramid.asy`)
    # Открываем PDF
    run(`xdg-open pyramid.pdf`)
end
# Запуск: сторона основания 6, высота 4
pyramid(6.0, 4.0)

