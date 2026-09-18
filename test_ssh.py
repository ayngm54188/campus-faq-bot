"""
test_ssh.py —— 验证 SSH 是否配置成功（对应手册第 4 步 ④）
运行：python test_ssh.py

如果输出「✅ SSH 连接成功」，说明你电脑已能和 GitHub 免密通信。
"""
import subprocess, sys

def main():
    print("正在测试与 GitHub 的 SSH 连接...\n")
    try:
        result = subprocess.run(
            ["ssh", "-T", "-o", "StrictHostKeyChecking=accept-new", "git@github.com"],
            capture_output=True, text=True, timeout=15,
        )
    except FileNotFoundError:
        print("❌ 未检测到 ssh 命令，请先安装 Git（git-scm.com）。")
        sys.exit(1)
    except Exception as e:
        print(f"⚠️ 测试时出错：{e}")
        sys.exit(1)

    out = result.stdout + result.stderr
    print(out)

    if "successfully authenticated" in out.lower() or "hi " in out.lower():
        print("✅ SSH 连接成功！你可以正常 git push 了。")
    else:
        print("❌ 未连接成功。请回到手册第 4 步，检查：")
        print("   1. 是否已生成密钥（~/.ssh/id_ed25519.pub 是否存在）")
        print("   2. 公钥是否完整粘贴到 GitHub → Settings → SSH keys")
        print("   3. 克隆仓库时是否用的是 git@github.com:... 的 SSH 地址")

if __name__ == "__main__":
    main()
