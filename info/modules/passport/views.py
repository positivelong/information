from flask import request
from flask import current_app
from flask import make_response
from flask import abort

from info import redis_store, constants
from info.utile.captcha.captcha import captcha
from . import passport_blu

@passport_blu.route('/image_code')
def get_image_code():
    """
    生成图片验证码并返回
    1. 取到参数
    2. 判断参数是否有值
    3. 生成图片验证码
    4. 保存图片验证码文字内容到redis
    5. 返回验证码图片
    :return:
    """
    # 1. 取到参数
    # args: 取到url中 ? 后面的参数
    image_code_id = request.args.get("imageCodeId", None)
    # 2. 判断参数是否有值
    if not image_code_id:
        return abort(403)
    # 3. 生成图片验证码
    name, text, image = captcha.generate_captcha()
    current_app.logger.debug("图片验证码是：%s" % text)
    # 4.保存图片验证码的文字内容到redis
    try:
        redis_store.set("ImageCodeId" + image_code_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        abort(500)
    # 5. 返回验证码图片
    response = make_response(image)
    # 设置数据的类型,以便浏览器更加智能识别是什么类型
    response.headers["Content-Type"] = "image/jpg"
    return response