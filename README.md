# KURASHI HACK（クラシハック）

「暮らしのちょっとした不満を、道具の力で解決する」をコンセプトにしたアフィリエイトメディアです。日々の生活で感じる「使いにくい」「片付かない」「掃除が面倒」といった小さなストレスを解消するアイテムを、実使用レビュー・リサーチをもとに紹介しています。

🔗 https://kurashi-hack.pages.dev

## 主な機能

- 記事一覧・カテゴリ別記事ページ
- サイト内検索（[Pagefind](https://pagefind.app/)によるビルド時インデックス生成）
- サイトマップ自動生成
- 楽天アフィリエイト・バリューコマース(Yahoo!ショッピング)対応の商品リンクコンポーネント

## 技術スタック

- **フレームワーク**: [Astro](https://astro.build/) 7
- **検索**: Pagefind
- **デプロイ**: Cloudflare Pages
- **記事**: `src/pages/article-*.astro`（Astroページとして直接管理）

## セットアップ

```bash
npm install
npm run dev
```

http://localhost:4321 で確認できます。

## ビルド

```bash
npm run build   # ./dist に出力（Pagefindインデックス含む）
npm run preview # ビルド結果をローカルで確認
```

## アフィリエイトID設定（任意）

`src/config/affiliates.ts` で楽天アフィリエイト・バリューコマースのIDを設定できます。未設定の場合はアフィリエイトIDなしの検索URLにフォールバックします。
