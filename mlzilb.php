<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $encoded_data = $_POST['encoded_data'];
    $decoded_data = base64_decode($encoded_data);
    $serialized_data = $decoded_data;
    $uncompressed_data = @zlib_decode($serialized_data);

    if ($uncompressed_data === false) {
        echo "解压缩数据时发生错误";
        exit;
    }

    $text_data = $uncompressed_data;
    $start_index = strpos($text_data, "<saveXml");
    $end_index = strpos($text_data, "</saveXml>", $start_index) + strlen("</saveXml>");
    $extracted_text = substr($text_data, $start_index, $end_index - $start_index);
    $text_data = $extracted_text;
    $text_data = str_replace('\\n', '\n', $text_data);

    // 清除解码文本中的 <s type="String" name="luserid">...</s>
    $decoded_text = preg_replace('/<s type="String" name="luserid">.*<\/s>/', '', $text_data);

    if ($decoded_text === $text_data) {
        echo "解码文本中没有需要清除的内容";
        $decoded_text = $text_data; // 没有清除内容，返回原始文本
    } else {
        echo "UID校验清理完成";
    }

    // 解析JSON数据
    $json_data = json_decode($decoded_text, true);
    if ($json_data !== null && isset($json_data['data'])) {
        $encoded_data = $json_data['data'];
    }
}
?>



<!DOCTYPE html>
<html>
<head>
    <title>解码存档数据</title>
    <style>
        body {
            background-color: #f6f6f6;
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 24px;
            text-align: center;
            margin-bottom: 20px;
        }

        label {
            font-weight: bold;
            display: block;
            margin-bottom: 10px;
        }

        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            resize: vertical;
        }

        input[type="submit"], input[type="button"] {
            background-color: #ff6600;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        .decoded-text {
            margin-top: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            background-color: #fff;
        }

        .json-button {
            background-color: #008000;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>解码存档数据</h1>
        <form method="post" action="">
            <label for="encoded_data">请输入4399的存档数据（可以解密部分数据）：</label>
            <textarea id="encoded_data" name="encoded_data" rows="5" cols="50"><?php echo isset($encoded_data) ? $encoded_data : ''; ?></textarea>
            <input type="submit" value="解码">
            <input type="button" class="json-button" value="解析JSON" onclick="parseJSON()">
        </form>

        <?php if (isset($decoded_text)) { ?>
            <div class="decoded-text">
                <h2>解码结果：</h2>
                <textarea rows="10" cols="50" readonly><?php echo $decoded_text; ?></textarea>
                <br>
                
            </div>
        <?php } ?>

        <script>
            function parseJSON() {
                var encodedData = document.getElementById('encoded_data').value;
                try {
                    var jsonData = JSON.parse(encodedData);
                    if (jsonData && jsonData.data) {
                        document.getElementById('encoded_data').value = jsonData.data;
                    }
                } catch (error) {
                    console.error('解析JSON失败:', error);
                }
            }
            
            function clearDecodedText() {
                document.querySelector('.decoded-text textarea').value = '';
            }
        </script>
    </div>
</body>
</html>

