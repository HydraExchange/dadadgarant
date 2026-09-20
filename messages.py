# Тексты на русском языке
RU_TEXTS = {
    "start_message": (
        "🇷🇺 PradaBuyers\n\n"
        "💎 Crypto OTC community\n"
        "🛡 Гарант сделок 24/7\n"
        "💰 Комиссия — всего 3%\n\n"
        "Крипта, подарки, NFT и другое.\n"
        "Создавай сделки в любое время через нашего гаранта.\n\n"
        "👥 Комьюнити — @PradaBuyers\n\n"
        "Выбери нужный раздел ниже:"
    ),
    "wallet_message": (
        "💼 Твой текущий кошелёк: {wallet}\n\n"
        "Отправь новый адрес кошелька для изменения "
        "или нажми кнопку ниже, чтобы вернуться в меню."
    ),
    "create_deal_message": (
        "📄 Создание сделки\n\n"
        "Введи сумму сделки в {valute}:\n"
        "`100.5`"
    ),
    "referral_message": (
        "🧷 Реферальная система\n\n"
        "🔗 Твоя реферальная ссылка:\n"
        "{referral_link}\n\n"
        "👥 Рефералов: 0\n"
        "💰 Заработано: 0 {valute}\n\n"
        "30% от комиссии бота"
    ),
    "change_lang_message": (
        "🌐 Выбери язык:"
    ),
    "lang_set_message": "🇷🇺 Язык изменён на русский.",
    "deal_created_message": (
        "✅ Сделка создана\n\n"
        "💰 Сумма: {amount} {valute}\n"
        "📜 Описание: {description}\n"
        "🔗 Ссылка для покупателя: {deal_link}"
    ),
    "payment_confirmed_message": (
        "✅ Оплата подтверждена\n\n"
        "🆔 Сделка #{deal_id}\n"
        "💰 Сумма: {amount} {valute}\n"
        "📜 Описание: {description}\n\n"
        "🔒 Сделка завершена."
    ),
    "payment_confirmed_seller_message": (
        "✅ Оплата подтверждена\n\n"
        "🆔 Сделка #{deal_id}\n"
        "📜 {description}\n\n"
        "🎁 Отправь подарок покупателю — @{buyer_username}\n\n"
        "⚠️ Перед отправкой обязательно проверь username покупателя. "
        "Если подарок отправлен другому человеку, возврата не будет."
    ),
    "seller_notification_message": (
        "👤 Пользователь @{buyer_username} присоединился "
        "к сделке #{deal_id}\n"
        "• Успешных сделок: {successful_deals}\n\n"
        "⚠️ Проверь, что это тот же пользователь, "
        "с которым ты вёл диалог ранее."
    ),
    "insufficient_balance_message": "❌ Недостаточно средств на балансе.",
    "wallet_updated_message": "✅ Кошелёк обновлён: {wallet}",
    "admin_panel_message": "⚙️ Админ-панель",
    "admin_view_deals_message": "📄 Активные сделки:\n{deals_list}",
    "admin_change_balance_message": (
        "Введите ID пользователя и новый баланс:\n"
        "`user_id баланс`"
    ),
    "admin_change_successful_deals_message": (
        "Введите ID пользователя и количество успешных сделок:\n"
        "`user_id количество`"
    ),
    "admin_change_valute_message": (
        "💱 Введите новую валюту:\n"
        "`USD / EUR / RUB`"
    ),
    "menu_button": "🔙 В меню",
    "pay_from_balance_button": "💳 Оплатить с баланса",
    "add_wallet_button": "🪙 Кошелёк",
    "create_deal_button": "📄 Создать сделку",
    "referral_button": "🧷 Рефералы",
    "change_lang_button": "🌐 Язык",
    "support_button": "📞 Поддержка",
    "english_lang_button": "🇬🇧 English",
    "russian_lang_button": "🇷🇺 Русский",
    "admin_view_deals_button": "📄 Просмотр сделок",
    "admin_change_balance_button": "💰 Изменить баланс",
    "admin_change_successful_deals_button": "📊 Успешные сделки",
    "admin_change_valute_button": "💱 Изменить валюту",
    "deal_info_message": (
        "💳 Сделка #{deal_id}\n\n"
        "👤 Ты покупатель в этой сделке.\n"
        "📌 Продавец: @{seller_username}\n"
        "• Успешных сделок: {successful_deals}\n\n"
        "📦 Ты покупаешь:\n"
        "{description}\n\n"
        "🏦 Адрес для оплаты:\n"
        "{wallet}\n\n"
        "💰 К оплате: {amount} {valute}\n"
        "📝 Memo: {deal_id}\n\n"
        "⚠️ Проверь адрес, сумму и memo перед оплатой.\n"
        "Memo обязателен.\n\n"
        "После оплаты дождись автоматического подтверждения."
    ),
    "awaiting_description_message": (
        "📝 Укажи, что ты предлагаешь в этой сделке:\n\n"
        "`Пример: 10 Caps + Pepe...`"
    ),
}


# Тексты на английском языке
EN_TEXTS = {
    "start_message": (
        "🇬🇧 PradaBuyers\n\n"
        "💎 Crypto OTC community\n"
        "🛡 24/7 deal guarantor\n"
        "💰 Fee — only 3%\n\n"
        "Crypto, gifts, NFTs & more.\n"
        "Create a deal anytime through our guarantor.\n\n"
        "👥 Community — @PradaBuyers\n\n"
        "Choose a section below:"
    ),
    "wallet_message": (
        "💼 Your current wallet: {wallet}\n\n"
        "Send a new wallet address to update it "
        "or use the button below to return to the menu."
    ),
    "create_deal_message": (
        "📄 Create deal\n\n"
        "Enter the deal amount in {valute}:\n"
        "`100.5`"
    ),
    "referral_message": (
        "🧷 Referral system\n\n"
        "🔗 Your referral link:\n"
        "{referral_link}\n\n"
        "👥 Referrals: 0\n"
        "💰 Earned: 0 {valute}\n\n"
        "30% of the bot's fee"
    ),
    "change_lang_message": (
        "🌐 Choose your language:"
    ),
    "lang_set_message": "🇬🇧 Language changed to English.",
    "deal_created_message": (
        "✅ Deal created\n\n"
        "💰 Amount: {amount} {valute}\n"
        "📜 Description: {description}\n"
        "🔗 Buyer link: {deal_link}"
    ),
    "payment_confirmed_message": (
        "✅ Payment confirmed\n\n"
        "🆔 Deal #{deal_id}\n"
        "💰 Amount: {amount} {valute}\n"
        "📜 Description: {description}\n\n"
        "🔒 Deal completed."
    ),
    "payment_confirmed_seller_message": (
        "✅ Payment confirmed\n\n"
        "🆔 Deal #{deal_id}\n"
        "📜 {description}\n\n"
        "🎁 Send the gift to the buyer — @{buyer_username}\n\n"
        "⚠️ Double-check the buyer's username before sending. "
        "There are no refunds if the gift is sent to someone else."
    ),
    "seller_notification_message": (
        "👤 @{buyer_username} joined deal #{deal_id}\n"
        "• Successful deals: {successful_deals}\n\n"
        "⚠️ Make sure this is the same user "
        "you were talking to earlier."
    ),
    "insufficient_balance_message": "❌ Insufficient balance.",
    "wallet_updated_message": "✅ Wallet updated: {wallet}",
    "admin_panel_message": "⚙️ Admin panel",
    "admin_view_deals_message": "📄 Active deals:\n{deals_list}",
    "admin_change_balance_message": (
        "Enter user ID and new balance:\n"
        "`user_id balance`"
    ),
    "admin_change_successful_deals_message": (
        "Enter user ID and number of successful deals:\n"
        "`user_id count`"
    ),
    "admin_change_valute_message": (
        "💱 Enter new currency:\n"
        "`USD / EUR / RUB`"
    ),
    "menu_button": "🔙 Back to menu",
    "pay_from_balance_button": "💳 Pay from balance",
    "add_wallet_button": "🪙 Wallet",
    "create_deal_button": "📄 Create deal",
    "referral_button": "🧷 Referrals",
    "change_lang_button": "🌐 Language",
    "support_button": "📞 Support",
    "english_lang_button": "🇬🇧 English",
    "russian_lang_button": "🇷🇺 Русский",
    "admin_view_deals_button": "📄 View deals",
    "admin_change_balance_button": "💰 Change balance",
    "admin_change_successful_deals_button": "📊 Successful deals",
    "admin_change_valute_button": "💱 Change currency",
    "deal_info_message": (
        "💳 Deal #{deal_id}\n\n"
        "👤 You are the buyer.\n"
        "📌 Seller: @{seller_username}\n"
        "• Successful deals: {successful_deals}\n\n"
        "📦 You are buying:\n"
        "{description}\n\n"
        "🏦 Payment address:\n"
        "{wallet}\n\n"
        "💰 Amount to pay: {amount} {valute}\n"
        "📝 Memo: {deal_id}\n\n"
        "⚠️ Check the address, amount and memo before paying.\n"
        "Memo is required.\n\n"
        "After payment, wait for automatic confirmation."
    ),
    "awaiting_description_message": (
        "📝 What are you offering in this deal?\n\n"
        "`Example: 10 Caps + Pepe...`"
    ),
}


# Функция для получения текста на выбранном языке
def get_text(lang, key, **kwargs):
    if lang == 'ru':
        return RU_TEXTS.get(key, '').format(**kwargs)
    elif lang == 'en':
        return EN_TEXTS.get(key, '').format(**kwargs)
    return ''