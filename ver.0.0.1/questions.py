# -*- coding: utf-8 -*-

QUESTIONS = [
    {
        "id": 1,
        "cat": "Developer Fundamentals",
        "text": "Apexで読み取り専用の変数を定義するためのキーワードは？",
        "options": ["A. static", "B. final", "C. private", "D. const"],
        "ans": "B",
        "exp": "finalキーワードは、一度割り当てられると変更できない変数を定義します。"
    },
    {
        "id": 2,
        "cat": "Testing, Debugging, Deployment",
        "text": "組織データへのアクセスを最小限にするためのテストアノテーションは？",
        "options": ["A. @isTest(SeeAllData=true)", "B. @isTest", "C. @TestVisible", "D. @isTest(SeeAllData=false)"],
        "ans": "D",
        "exp": "SeeAllData=falseがデフォルトであり、テストデータの隔離を推奨します。"
    },
    {
        "id": 3,
        "cat": "User Interface",
        "text": "LWCでJavaScriptプロパティをHTMLにバインドする記法は？",
        "options": ["A. {!prop}", "B. {prop}", "C. [[prop]]", "D. {{prop}}"],
        "ans": "B",
        "exp": "LWCでは単一の中括弧を使用してバインドします。"
    },
    {
        "id": 4,
        "cat": "Process Automation and Logic",
        "text": "1対多のリレーションで子レコードが削除された際、親も削除されるのは？",
        "options": ["A. 参照関係", "B. 外部ID", "C. 主従関係", "D. 階層関係"],
        "ans": "C",
        "exp": "主従関係では、主レコードの削除が従レコードに波及します。"
    },
    {
        "id": 5,
        "cat": "Developer Fundamentals",
        "text": "SOQLクエリをループ内で実行してはいけない理由（ガバナ制限）は？",
        "options": ["A. CPU時間", "B. 100クエリ制限", "C. ヒープサイズ", "D. DML制限"],
        "ans": "B",
        "exp": "単一トランザクション内でのSOQLクエリ数は最大100回です（同期処理）。"
    },
    # 必要に応じて100問まで追加
]
