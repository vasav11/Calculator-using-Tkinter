class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

    def create_display_labels(self):
        total_label=tk.Label(self.dispaly_frame, text=self.total_expression,anchor=tk.E,bg=LIGHT_GRAY,FG=LABEL_COLOR,PADX=24 ,fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        label=tk.pack(expand=True, fill='both')
        total_label = tk.Label(self.dispaly_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               FG=LABEL_COLOR, PADX=24, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label,label


    def create_display_frame(self):
            frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
            frame.pack(expand=True, fill="both")
            return frame

def create_button_labels(self):
    frame = tk.Frame(self.window)
    frame.pack(expand=True, fill="both")
    return frame

def run(self):
    self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
