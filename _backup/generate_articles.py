import os
import re

template_file = "article-footrest.html"
with open(template_file, "r", encoding="utf-8") as f:
    template = f.read()

articles = [
    {
        "file": "article-cable-box.html",
        "category": "デスク周り",
        "title": "【配線隠し】デスク下用ケーブルボックスおすすめ3選！ごちゃつくコードをスッキリ収納",
        "desc": "デスク周りの配線がごちゃごちゃして掃除が面倒ではありませんか？床置きできるおしゃれなケーブルボックスで、足元をスッキリさせましょう。",
        "breadcrumb": "ホーム</a> > デスク周り > ケーブルボックス",
        "h1": "【配線隠し】デスク下用ケーブルボックスおすすめ3選！ごちゃつくコードをスッキリ収納",
        "img": "assets/cable_box.jpg",
        "img_alt": "ケーブルボックス",
        "p1": "テレワーク環境を整えると、パソコン、モニター、スマホの充電器など、ケーブル類がどんどん増えていきますよね。",
        "p2": "足元で絡まったコードは見た目が悪いだけでなく、ホコリが溜まってトラッキング現象（火災の原因）を引き起こす危険もあります。おしゃれなケーブルボックスにコンセントをまるごと隠すだけで、安全で掃除しやすい空間に生まれ変わります。",
        "table_headers": ["", "山崎実業 (Yamazaki)<br>ケーブルボックス ウェブ L", "サンワダイレクト<br>ケーブルボックス 木製", "イノマタ化学<br>テーブルタップボックス"],
        "table_row1": ["インテリアに馴染む洗練デザイン", "温かみのあるリアル木目", "圧倒的なコスパとシンプルさ"],
        "table_row2": ["約3,000円〜", "約3,980円〜", "約1,200円〜"],
        "product_name": "山崎実業 (Yamazaki) ケーブルボックス ウェブ L",
        "product_desc": "どんな部屋にも自然に馴染む、シンプルで美しいデザインのケーブルボックス。プラスチック製ですがマットな質感で安っぽく見えません。",
        "pro1": "ホコリが入りにくい設計",
        "pro2": "上部にスマホを置いて充電可能",
        "pro3": "お手入れが簡単な素材",
        "con": "大きなACアダプターは入りきらない場合がある",
        "link": "https://www.amazon.co.jp/s?k=%E3%82%B1%E3%83%BC%E3%83%96%E3%83%AB%E3%83%9C%E3%83%83%E3%82%AF%E3%82%B9"
    },
    {
        "file": "article-hanger-rack.html",
        "category": "収納",
        "title": "【省スペース】スリムでおしゃれなハンガーラックおすすめ3選！一人暮らしの部屋を広く見せる",
        "desc": "コートやカバンをちょい置きする場所がなくて困っていませんか？壁際にすっきり置けるスリムなハンガーラックでお部屋を整理しましょう。",
        "breadcrumb": "ホーム</a> > 収納 > ハンガーラック",
        "h1": "【省スペース】スリムでおしゃれなハンガーラックおすすめ3選！一人暮らしの部屋を広く見せる",
        "img": "assets/hanger_rack.jpg",
        "img_alt": "ハンガーラック",
        "p1": "外から帰ってきた時、ついコートやジャケットをソファやベッドの上に脱ぎっぱなしにしていませんか？",
        "p2": "一人暮らしの限られたスペースでも、奥行きの浅いスリムなハンガーラックを1つ置くだけで、部屋が驚くほど片付いて見えます。来客用の一時置き場としても大活躍します。",
        "table_headers": ["", "山崎実業 (Yamazaki)<br>スリムコートハンガー", "萩原 (HAGIHARA)<br>ハンガーラック 木製", "アイリスオーヤマ<br>スタイルハンガー"],
        "table_row1": ["壁に立てかけるだけの超省スペース", "折りたためる天然木素材", "棚付きで小物も置ける"],
        "table_row2": ["約3,300円〜", "約4,500円〜", "約3,000円〜"],
        "product_name": "山崎実業 (Yamazaki) スリムコートハンガー",
        "product_desc": "壁に立てかけるだけでどこでもハンガースペースが作れる魔法のようなアイテム。スチールと天然木の組み合わせがとてもおしゃれです。",
        "pro1": "場所をとらない究極のスリム設計",
        "pro2": "移動が簡単でどこにでも置ける",
        "pro3": "生活感を出さない美しいデザイン",
        "con": "大量の服を掛けるのには向いていない",
        "link": "https://www.amazon.co.jp/s?k=%E3%83%8F%E3%83%B3%E3%82%AC%E3%83%BC%E3%83%A9%E3%83%83%E3%82%AF"
    },
    {
        "file": "article-gap-wagon.html",
        "category": "キッチン",
        "title": "【デッドスペース活用】すき間収納ワゴンおすすめ3選！冷蔵庫横を便利に",
        "desc": "冷蔵庫と壁の間のわずかな隙間、もったいないと思っていませんか？幅10cm台から置けるスリムな収納ワゴンで、キッチンの収納力をアップさせましょう。",
        "breadcrumb": "ホーム</a> > キッチン > すき間収納",
        "h1": "【デッドスペース活用】すき間収納ワゴンおすすめ3選！冷蔵庫横を便利に",
        "img": "assets/gap_wagon.jpg",
        "img_alt": "すき間収納ワゴン",
        "p1": "キッチンの冷蔵庫横やシンク横にある、10〜20cm程度の微妙な隙間。ここをそのままにしておくのは非常にもったいないです！",
        "p2": "キャスター付きの「すき間収納ワゴン」を活用すれば、調味料やストック食材、ペットボトルなどをたっぷり収納でき、キッチンが劇的に使いやすくなります。",
        "table_headers": ["", "山崎実業 (Yamazaki)<br>ハンドル付きスリムワゴン", "不二貿易<br>スリム ワゴン 幅12cm", "平安伸銅工業<br>すき間収納ワゴン"],
        "table_row1": ["木製天板がおしゃれな大本命", "通気性の良いメッシュ仕様", "水に強いシンプル設計"],
        "table_row2": ["約11,000円〜", "約3,000円〜", "約2,500円〜"],
        "product_name": "山崎実業 (Yamazaki) ハンドル付きスリムワゴン",
        "product_desc": "幅わずか13cmで、どんな隙間にもスッと入り込む優れもの。ハンドル付きなので引き出しやすく、目隠しにもなるのでキッチンがすっきり見えます。",
        "pro1": "中身を隠せるスマートなデザイン",
        "pro2": "木製天板に小物を置ける",
        "pro3": "丈夫なスチール製",
        "con": "価格が少し高め",
        "link": "https://www.amazon.co.jp/s?k=%E3%81%99%E3%81%8D%E9%96%93%E5%8F%8E%E7%B4%8D+%E3%83%AF%E3%82%B4%E3%83%B3"
    },
    {
        "file": "article-vacuum-stand.html",
        "category": "リビング",
        "title": "【壁に穴を開けない】コードレス掃除機スタンドおすすめ3選！おしゃれに収納",
        "desc": "ダイソンなどのコードレス掃除機、壁に穴を開けずに収納したいですよね。賃貸でも安心な自立式クリーナースタンドを比較しました。",
        "breadcrumb": "ホーム</a> > リビング > 掃除機スタンド",
        "h1": "【壁に穴を開けない】コードレス掃除機スタンドおすすめ3選！おしゃれに収納",
        "img": "assets/vacuum_stand.jpg",
        "img_alt": "掃除機スタンド",
        "p1": "コードレス掃除機はサッと使えて便利ですが、「壁に穴を開けてブラケットを固定しなければならない」のが賃貸住宅では大きなネックになります。",
        "p2": "自立式のクリーナースタンドを使えば、壁を傷つけずに充電もでき、付属のノズルパーツなどもまとめて美しく収納できます。",
        "table_headers": ["", "山崎実業 (Yamazaki)<br>クリーナースタンド", "サンワダイレクト<br>ダイソン 掃除機スタンド", "EQUALS WALL<br>クリーナースタンド"],
        "table_row1": ["パーツも全て収納できる完璧な設計", "木目調で温かみのあるデザイン", "スタイリッシュな極薄ベース"],
        "table_row2": ["約6,000円〜", "約4,500円〜", "約12,000円〜"],
        "product_name": "山崎実業 (Yamazaki) コードレスクリーナースタンド",
        "product_desc": "掃除機本体だけでなく、様々なアタッチメントパーツを全て裏側に収納できる機能性の高さが魅力。壁に穴を開けずに、美しくまとまります。",
        "pro1": "壁に穴を開けずに設置可能",
        "pro2": "全てのパーツを一括収納",
        "pro3": "安定感のある頑丈な作り",
        "con": "対応機種を確認する必要がある",
        "link": "https://www.amazon.co.jp/s?k=%E3%82%B3%E3%83%BC%E3%83%89%E3%83%AC%E3%82%B9%E6%8E%83%E9%99%A4%E6%A9%9F+%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%89"
    },
    {
        "file": "article-bed-storage.html",
        "category": "収納",
        "title": "【キャスター付き】ベッド下収納ケースおすすめ3選！ホコリを防いで衣類を整理",
        "desc": "ベッドの下を有効活用できていますか？キャスター付きで引き出しやすい収納ケースで、シーズンオフの衣類をスッキリ片付けましょう。",
        "breadcrumb": "ホーム</a> > 収納 > ベッド下収納",
        "h1": "【キャスター付き】ベッド下収納ケースおすすめ3選！ホコリを防いで衣類を整理",
        "img": "assets/bed_storage.jpg",
        "img_alt": "ベッド下収納",
        "p1": "お部屋の収納スペースが足りないと感じたら、まずは「ベッドの下」を見直してみてください。ここは衣類や布団などの大物をしまうのに最適なスペースです。",
        "p2": "ただし、ホコリが溜まりやすいため、フタ付き・キャスター付きの収納ケースを選ぶのが鉄則です。引き出しやすさとお手入れのしやすさがポイントです。",
        "table_headers": ["", "天馬 (Tenma)<br>ロックス ベッド下収納", "アイリスオーヤマ<br>ベッド下収納ボックス", "無印良品<br>ポリプロピレン衣装ケース"],
        "table_row1": ["頑丈で長く使える大定番", "コスパ重視のシンプル設計", "無駄のない美しいフォルム"],
        "table_row2": ["約3,500円〜", "約2,500円〜", "約2,000円〜"],
        "product_name": "天馬 (Tenma) ロックス ベッド下収納",
        "product_desc": "収納ケースの定番メーカー「天馬」のベッド下専用ケース。キャスターの動きがスムーズで、フタがしっかり閉まるのでホコリを完全にシャットアウトします。",
        "pro1": "頑丈でたわまない確かな品質",
        "pro2": "両開きフタで出し入れが楽",
        "pro3": "キャスターの方向を変更可能",
        "con": "デザインが実用性重視",
        "link": "https://www.amazon.co.jp/s?k=%E3%83%99%E3%83%83%E3%83%89%E4%B8%8B%E5%8F%8E%E7%B4%8D+%E3%82%B1%E3%83%BC%E3%82%B9"
    },
    {
        "file": "article-bath-mat.html",
        "category": "お風呂・洗面所",
        "title": "【お手入れ不要】珪藻土バスマットおすすめ3選！割れない・冷たくない進化系",
        "desc": "洗濯の手間から解放される珪藻土バスマット。最近は「割れない」「冬でも冷たくない」ソフトタイプの珪藻土マットが大人気です。",
        "breadcrumb": "ホーム</a> > お風呂・洗面所 > 珪藻土バスマット",
        "h1": "【お手入れ不要】珪藻土バスマットおすすめ3選！割れない・冷たくない進化系",
        "img": "assets/bath_mat.jpg",
        "img_alt": "珪藻土バスマット",
        "p1": "布製のバスマットは、家族全員で使うと最後にはビショビショになり、頻繁に洗濯するのも面倒ですよね。",
        "p2": "「珪藻土バスマット」なら一瞬で足裏の水分を吸い取ってくれます。さらに最近は、従来の硬いボード型の欠点（割れる・冷たい）を克服した「ソフトタイプ」が主流になってきており、快適さが格段に向上しています。",
        "table_headers": ["", "＋d (プラスディー)<br>珪藻土バスマット", "アイリスオーヤマ<br>珪藻土バスマット ソフト", "ニトリ<br>珪藻土バスマット"],
        "table_row1": ["おしゃれなデザインと高い吸水性", "丸めて収納できるソフトタイプ", "手軽に買えるコスパの良さ"],
        "table_row2": ["約5,000円〜", "約2,500円〜", "約1,500円〜"],
        "product_name": "アイリスオーヤマ 珪藻土バスマット ソフト",
        "product_desc": "アスベスト不使用で安全性が高く、丸めてコンパクトに収納できるソフトタイプの珪藻土バスマット。冬場でも足がヒヤッとしないのが嬉しいポイントです。",
        "pro1": "柔らかいので割れる心配がゼロ",
        "pro2": "冬でも冷たくない",
        "pro3": "使用後は丸めて隙間に立てておける",
        "con": "長期間使うと吸水力が落ちてくることがある",
        "link": "https://www.amazon.co.jp/s?k=%E7%8F%AA%E8%97%BB%E5%9C%9F%E3%83%90%E3%82%B9%E3%83%9E%E3%83%83%E3%83%88"
    }
]

import re

for art in articles:
    content = template
    # Title & Meta
    content = re.sub(r'<title>.*?</title>', f'<title>{art["title"]} - KURASHI HACK</title>', content)
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{art["desc"]}">', content)
    # Breadcrumb
    content = re.sub(r'ホーム</a> > .*?\n', f'{art["breadcrumb"]}\n', content)
    # H1
    content = re.sub(r'<h1 class="post-title">.*?</h1>', f'<h1 class="post-title">{art["h1"]}</h1>', content)
    # Image
    content = re.sub(r'<img src="assets/footrest.jpg" alt=".*?">', f'<img src="{art["img"]}" alt="{art["img_alt"]}">', content)
    # Paragraphs (Assume there are two <p> before <div class="alert">)
    # We will do a generic replacement for the intro text.
    intro_pattern = r'<div class="post-content">\s*<p>.*?</p>\s*<p>.*?</p>'
    new_intro = f'<div class="post-content">\n                    <p>{art["p1"]}</p>\n                    <p>{art["p2"]}</p>'
    content = re.sub(intro_pattern, new_intro, content, flags=re.DOTALL)
    
    # Table headers
    headers_pattern = r'<tr>\s*<th></th>\s*<th>.*?</th>\s*<th>.*?</th>\s*<th>.*?</th>\s*</tr>'
    new_headers = f'<tr>\n                                    <th></th>\n                                    <th>{art["table_headers"][1]}</th>\n                                    <th>{art["table_headers"][2]}</th>\n                                    <th>{art["table_headers"][3]}</th>\n                                </tr>'
    content = re.sub(headers_pattern, new_headers, content, flags=re.DOTALL)
    
    # Table row 1 (特徴)
    tr1_pattern = r'<tr>\s*<th>特徴</th>\s*<td class="highlight">.*?</td>\s*<td>.*?</td>\s*<td>.*?</td>\s*</tr>'
    new_tr1 = f'<tr>\n                                    <th>特徴</th>\n                                    <td class="highlight">{art["table_row1"][0]}</td>\n                                    <td>{art["table_row1"][1]}</td>\n                                    <td>{art["table_row1"][2]}</td>\n                                </tr>'
    content = re.sub(tr1_pattern, new_tr1, content, flags=re.DOTALL)
    
    # Table row 2 is "素材" in template, let's just make it price for simplicity or replace entire tbody content
    # Let's replace the price row (which is the 4th row)
    price_pattern = r'<tr>\s*<th>価格帯（目安）</th>\s*<td>.*?</td>\s*<td>.*?</td>\s*<td>.*?</td>\s*</tr>'
    new_price = f'<tr>\n                                    <th>価格帯（目安）</th>\n                                    <td>{art["table_row2"][0]}</td>\n                                    <td>{art["table_row2"][1]}</td>\n                                    <td>{art["table_row2"][2]}</td>\n                                </tr>'
    content = re.sub(price_pattern, new_price, content, flags=re.DOTALL)
    
    # Product Title
    content = re.sub(r'<h2>1位：.*?</h2>', f'<h2>1位：{art["product_name"]}</h2>', content)
    # Product Desc
    # We replace the text in <div class="product-body"> <p>
    pb_pattern = r'<div class="product-body">\s*<p>.*?</p>'
    new_pb = f'<div class="product-body">\n                            <p>{art["product_desc"]}</p>'
    content = re.sub(pb_pattern, new_pb, content, flags=re.DOTALL)
    
    # Pros
    pros_pattern = r'<h4>ここが最高！</h4>\s*<ul>\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>'
    new_pros = f'<h4>ここが最高！</h4>\n                                    <ul>\n                                        <li>{art["pro1"]}</li>\n                                        <li>{art["pro2"]}</li>\n                                        <li>{art["pro3"]}</li>\n                                    </ul>'
    content = re.sub(pros_pattern, new_pros, content, flags=re.DOTALL)
    
    # Cons
    cons_pattern = r'<h4>注意点</h4>\s*<ul>\s*<li>.*?</li>\s*</ul>'
    new_cons = f'<h4>注意点</h4>\n                                    <ul>\n                                        <li>{art["con"]}</li>\n                                    </ul>'
    content = re.sub(cons_pattern, new_cons, content, flags=re.DOTALL)
    
    # Link
    content = re.sub(r'href="https://www.amazon.co.jp/s\?k=.*?" target="_blank"', f'href="{art["link"]}" target="_blank"', content)
    
    with open(art["file"], "w", encoding="utf-8") as f:
        f.write(content)

print("Created 6 articles.")
