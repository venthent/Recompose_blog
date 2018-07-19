class Config:
    '''
    在 3 个子类中, SQLALCHEMY_DATABASE_URI 变量都被指定了不同的值。这样程序就可在不同
    的配置环境中运行,每个环境都使用不同的数据库。
    '''
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:1111@localhost/BLOG"
    DEBUG=True
    @staticmethod
    def init_app(app):
        '''在这个方法中,可以执行对当前
环境的配置初始化'''
        pass

config={
    'default':Config,
}