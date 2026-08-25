// 楽天アフィリエイト・バリューコマース(Yahoo!ショッピング)のID設定
// 未設定（空文字）のままなら、AffiliateLinkコンポーネントは
// 従来通りのアフィリエイトID無しの検索URLを出力する（安全なフォールバック）。

// 楽天アフィリエイトの管理画面「リンクジェネレーター」または「サーチリンク作成」で
// 任意のURLを1件変換し、生成されたURLの `?pc=` より前の部分を貼り付ける。
// 例: "https://hb.afl.rakuten.co.jp/hgc/xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx/"
export const RAKUTEN_LINK_PREFIX = "";

// バリューコマース管理画面「サイト管理」で確認できるサイトID
export const VALUECOMMERCE_SID = "";

// バリューコマースのYahoo!ショッピング提携プログラム詳細ページで確認できるプログラムID
export const VALUECOMMERCE_YAHOO_PID = "";
