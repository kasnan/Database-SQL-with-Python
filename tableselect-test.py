import tkinter as tk  # 툴킷 인터페이스
import tkinter.ttk as ttk  # tk의 확장 (트리뷰, 콤보박스 등 제공)

window = tk.Tk()

window.geometry("400x200+50+50")
window.title("창 타이틀")

frame = tk.Frame(window)
frame.pack()

tree = ttk.Treeview(frame, columns=(1, 2, 3), height=5, show="headings")
tree.pack(side='left')

# 필드명
tree.heading(1, text="A")
tree.heading(2, text="B")
tree.heading(3, text="C")

# 기본 너비
tree.column(1, width=100)
tree.column(2, width=100)
tree.column(3, width=100)

# 테이블 스크롤바 표시
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')
tree.configure(yscrollcommand=scroll.set)

# 기본 데이터 추가
data = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["10", "11", "12"],
        ["13", "14", "15"],
        ["16", "17", "18"]]

for val in data:
    tree.insert('', 'end', values=(val[0], val[1], val[2]))

# 라벨 기본값
label = tk.Label(window, text="default text")
label.pack()

# 테이블 항목 클릭시 click_item 호출


def click_item(event):
    selectedItem = tree.focus()
    getValue = tree.item(selectedItem).get('values')  # 딕셔너리의 값만 가져오기
    label.configure(text=getValue)  # 라벨 내용 바꾸기


tree.bind('<ButtonRelease-1>', click_item)

window.mainloop()