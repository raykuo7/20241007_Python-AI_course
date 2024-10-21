from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)

        # Top frame with three buttons
        topFrame = ttk.Frame(self, borderwidth=1, relief='groove')
        btn1 = ttk.Button(topFrame, text="按鈕1")
        btn1.pack(side='left', expand=True, fill='x', padx=10, ipady=10)  # Increase button height with ipady
        btn2 = ttk.Button(topFrame, text="按鈕2")
        btn2.pack(side='left', expand=True, fill='x', padx=10, ipady=10)  # Increase button height with ipady
        btn3 = ttk.Button(topFrame, text="按鈕3")
        btn3.pack(side='left', expand=True, fill='x', padx=10, ipady=10)  # Increase button height with ipady
        topFrame.pack(padx=10, pady=(10, 0), ipadx=10, ipady=10, expand=True, fill='x')

        # Bottom frame with three inner frames
        bottomFrame = ttk.Frame(self, borderwidth=1, relief='groove')
        bottomFrame.pack(padx=10, pady=10, expand=True, fill='x')

        f1 = ttk.Frame(bottomFrame, borderwidth=3, relief='groove', padding=10)
        f2 = ttk.Frame(bottomFrame, borderwidth=3, relief='groove', padding=10)
        f3 = ttk.Frame(bottomFrame, borderwidth=3, relief='groove', padding=10)
        f1.pack(side='left', expand=True, fill='both', padx=10)
        f2.pack(side='left', expand=True, fill='both', padx=10)
        f3.pack(side='left', expand=True, fill='both', padx=10)

        # Buttons in the first column (f1)
        btna1 = ttk.Button(f1, text="大的")
        btna1.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady
        btna2 = ttk.Button(f1, text="大的")
        btna2.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady
        btna3 = ttk.Button(f1, text="大的")
        btna3.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady

        # Buttons in the second column (f2)
        btnb1 = ttk.Button(f2, text="大的")
        btnb1.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady
        btnb2 = ttk.Button(f2, text="大的")
        btnb2.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady
        btnb3 = ttk.Button(f2, text="大的")
        btnb3.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady

        # Buttons in the third column (f3)
        btnc1 = ttk.Button(f3, text="大的")
        btnc1.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady
        btnc2 = ttk.Button(f3, text="大的")
        btnc2.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady
        btnc3 = ttk.Button(f3, text="大的")
        btnc3.pack(expand=True, fill='both', pady=5, ipady=20)  # Increase button height with ipady


def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
