.data
x dw 0
y dw 0
ok db 0
t_0 dw 0
t_1 dw 0
t_2 db 0
_str_0 db "valor aceito", 0
_str_1 db "valor baixo", 0

.code
START:
    call _read_integer
    mov word ptr [x], ax
    mov ax, word ptr [x]
    shl ax, 1
    mov word ptr [t_0], ax
    mov ax, word ptr [t_0]
    add ax, 1
    mov word ptr [t_1], ax
    mov ax, word ptr [t_1]
    mov word ptr [y], ax
    mov ax, word ptr [y]
    cmp ax, 10
    setge al
    mov byte ptr [t_2], al
    mov al, byte ptr [t_2]
    mov byte ptr [ok], al
    mov al, byte ptr [ok]
    cmp al, 0
    je L_ELSE_0
    push offset _str_0
    call _print_string
    push word ptr [y]
    call _print_integer
    jmp L_END_1
L_ELSE_0:
    push offset _str_1
    call _print_string
L_END_1:
    hlt
END START
