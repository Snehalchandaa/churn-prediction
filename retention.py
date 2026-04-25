# def get_action(prob, clv, engagement, cart):
#
#     if prob > 0.8:
#         if clv > 3000:
#             return " High-value: 25% discount + personal call"
#         return "Medium value: 15% discount"
#
#     elif prob > 0.6:
#         return " Re-engagement email + product recommendations"
#
#     elif cart > 0.7:
#         return " Cart reminder + coupon"
#
#     elif engagement < 0.3:
#         return " Low engagement: win-back campaign"
#
#     else:
#         return "No action needed"


# def get_action(prob, clv, engagement, cart):

#     if prob > 0.8:
#         return "30% Discount + Personal Call"
#     elif prob > 0.6:
#         return "Re-engagement Email"
#     elif cart > 0.7:
#         return " Cart Reminder Offer"
#     elif engagement < 0.3:
#         return " Win-back Campaign"
#     else:
#         return " No Action Needed"

def get_reason(recency, engagement, cart, email):

    if recency > 200:
        return "Customer inactivity detected (high recency)"

    elif cart > 0.7:
        return "High cart abandonment indicating purchase hesitation"

    elif email < 0.2:
        return "Low email engagement (campaigns not effective)"

    elif engagement < 0.3:
        return "Low platform engagement"

    else:
        return "General behavioral decline"


def get_action(prob, clv, engagement, cart):

    # 🔴 CRITICAL CHURN
    if prob > 0.8:
        if clv > 5000:
            return {
                "segment": "Critical - High Value",
                "priority": "Urgent",
                "offer": "30% retention incentive + dedicated account manager call",
                "channel": "Phone + Email",
                "campaign": "VIP Retention Campaign"
            }
        else:
            return {
                "segment": "Critical",
                "priority": "High",
                "offer": "20% discount + limited-time offer",
                "channel": "Email + SMS",
                "campaign": "Churn Recovery Campaign"
            }

    # 🟠 HIGH RISK
    elif prob > 0.6:
        if cart > 0.7:
            return {
                "segment": "High Risk",
                "priority": "High",
                "offer": "Cart recovery offer + free shipping",
                "channel": "Email + Push Notification",
                "campaign": "Cart Abandonment Recovery"
            }
        else:
            return {
                "segment": "High Risk",
                "priority": "Medium",
                "offer": "Personalized product recommendations",
                "channel": "Email",
                "campaign": "Re-engagement Campaign"
            }

    # 🟡 MEDIUM RISK
    elif prob > 0.4:
        return {
            "segment": "Medium Risk",
            "priority": "Medium",
            "offer": "Targeted offers on frequently viewed categories",
            "channel": "Email",
            "campaign": "Engagement Boost Campaign"
        }

    # 🟢 LOW RISK (FIXED HERE)
    else:
        return {
            "segment": "Low Risk",
            "priority": "Low",
            "offer": "Loyalty rewards + early access to new products",
            "channel": "Email",
            "campaign": "Loyalty & Upsell Campaign"
        }

def recommend_products(segment):

    if "Critical" in segment:
        return ["Discount Bundle Pack", "Top Trending Products"]

    elif "High Risk" in segment:
        return ["Popular Items", "Recently Viewed Products"]

    else:
        return ["Premium Products", "New Arrivals"]