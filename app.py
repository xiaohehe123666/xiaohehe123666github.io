from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# ===== 模拟功能函数（真实执行逻辑）=====
def organize_files():
    return "✔ 已模拟整理文件（真实环境可操作目录）"

def calculate_expense():
    data = {"吃饭": 30, "交通": 10}
    total = sum(data.values())
    return f"✔ 总支出：{total}"

def countdown():
    return "✔ 倒计时完成（示例）"

def generate_password():
    import random, string
    pwd = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    return f"✔ 密码：{pwd}"

# ===== API 映射 =====
functions = {
    "整理桌面文件": organize_files,
    "统计开销": calculate_expense,
    "倒计时": countdown,
    "生成密码": generate_password
}

@app.route("/run/<name>")
def run(name):
    if name in functions:
        result = functions[name]()
        return jsonify({"result": result})
    return jsonify({"result": "❌ 未找到功能"})

# ===== 页面 =====
html = """
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<title>Python 生活工具</title>

<style>
body {
    background:#0f172a;
    color:white;
    font-family:Arial;
    padding:20px;
}

.card {
    background:#1e293b;
    padding:15px;
    margin-bottom:10px;
    border-radius:10px;
}

button {
    margin-top:10px;
    padding:5px 10px;
}
</style>
</head>

<body>

<h1>Python 实用工具（可运行版）</h1>

<div id="list"></div>

<script>

const data = [
"整理桌面文件",
"统计开销",
"倒计时",
"生成密码"
];

function render(){
    let html="";
    data.forEach(d=>{
        html += `
        <div class="card">
            <h3>${d}</h3>
            <button onclick="run('${d}')">运行</button>
            <div id="${d}"></div>
        </div>
        `;
    });
    document.getElementById("list").innerHTML = html;
}

function run(name){
    fetch("/run/" + name)
    .then(res=>res.json())
    .then(data=>{
        document.getElementById(name).innerText = data.result;
    });
}

render();

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)