from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views as MainApp
admin.site.site_header = "Essence"
admin.site.site_title = "Essence Admin Portal"
admin.site.index_title = "Welcome to Essence Admin Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",MainApp.homePage),
    path("checkout/",MainApp.checkoutPage),
    path("contact/",MainApp.contactPage),
    path("regular-page/",MainApp.regularPage),
    path("shop/<str:mc>/<str:sc>/<str:br>/",MainApp.shopPage),
    path("single-blog/",MainApp.singleblogPage),
    path("single-product/<int:num>/",MainApp.singleproductPage),
    path("price-filter/<str:mc>/<str:sc>/<str:br>/",MainApp.priceFilterPage),
    path("sort-filter/<str:mc>/<str:sc>/<str:br>/",MainApp.sortFilterPage),
    path("search/",MainApp.searchPage),
    path("login/",MainApp.loginPage),
    path("signup/",MainApp.signupPage),
    path("logout/",MainApp.logoutPage),
    path("profile/",MainApp.profilePage),
    path("update-profile/",MainApp.updateProfilePage),
    path("add-to-cart/<int:num>/",MainApp.addToCartPage),
    path("cart/",MainApp.cartPage),
    path("delete-cart/<str:id>/",MainApp.deleteCartPage),
    path("update-cart/<str:id>/<str:op>/",MainApp.updateCartPage),
    path("place-order/",MainApp.placeOrderPage),
    path("confirmation/",MainApp.confirmationPage),
    path("add-to-wishlist/<int:num>/",MainApp.addtoWishlistPage),
    path("delete-wishlist/<int:num>/",MainApp.deleteWishlistPage),
    path("forgot-1/",MainApp.forgotPasswordPage1),
    path("forgot-2/",MainApp.forgotPasswordPage2),
    path("forgot-3/",MainApp.forgotPasswordPage3),
    path("paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>",MainApp.paymentSuccess),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
