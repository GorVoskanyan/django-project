SELECT "shop_product"."id",
       "shop_product"."name",
       "shop_product"."description",
       "shop_product"."price",
       "shop_product"."discount",
       "shop_product"."created_at",
       "shop_product"."archived",
       "shop_product"."preview"
FROM "shop_product"
WHERE NOT "shop_product"."archived"
ORDER BY "shop_product"."name" ASC, "shop_product"."price" ASC;

--
SELECT "shop_product"."id",
       "shop_product"."name",
       "shop_product"."description",
       "shop_product"."price",
       "shop_product"."discount",
       "shop_product"."created_at",
       "shop_product"."archived",
       "shop_product"."preview"
FROM "shop_product"
WHERE "shop_product"."id" = 1
LIMIT 21;

SELECT "shop_productimage"."id",
       "shop_productimage"."product_id",
       "shop_productimage"."image",
       "shop_productimage"."description"
FROM "shop_productimage"
WHERE "shop_productimage"."product_id" = 1;


--
SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2024-04-12 06:38:39.586514' AND
       "django_session"."session_key" = 'i2bbx6ps4ai5sdn3v1vpi4hry2x9gy8n')
LIMIT 21;

SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shop_order"."id",
       "shop_order"."delivery_address",
       "shop_order"."promocode",
       "shop_order"."created_at",
       "shop_order"."user_id",
       "shop_order"."receipt",
       "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "shop_order"
         INNER JOIN "auth_user" ON ("shop_order"."user_id" = "auth_user"."id");


--
SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2024-04-12 06:42:41.720329' AND
       "django_session"."session_key" = 'i2bbx6ps4ai5sdn3v1vpi4hry2x9gy8n')
LIMIT 21;

SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shop_order"."id",
       "shop_order"."delivery_address",
       "shop_order"."promocode",
       "shop_order"."created_at",
       "shop_order"."user_id",
       "shop_order"."receipt",
       "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "shop_order"
         INNER JOIN "auth_user" ON ("shop_order"."user_id" = "auth_user"."id");

SELECT ("shop_order_products"."order_id") AS "_prefetch_related_val_order_id",
       "shop_product"."id",
       "shop_product"."name",
       "shop_product"."description",
       "shop_product"."price",
       "shop_product"."discount",
       "shop_product"."created_at",
       "shop_product"."archived",
       "shop_product"."preview"
FROM "shop_product"
         INNER JOIN "shop_order_products" ON ("shop_product"."id" = "shop_order_products"."product_id")
WHERE "shop_order_products"."order_id" IN (1)
ORDER BY "shop_product"."name" ASC, "shop_product"."price" ASC;


--
SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2024-04-12 06:46:18.623876' AND
       "django_session"."session_key" = 'i2bbx6ps4ai5sdn3v1vpi4hry2x9gy8n')
LIMIT 21;

SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shop_order"."id",
       "shop_order"."delivery_address",
       "shop_order"."promocode",
       "shop_order"."created_at",
       "shop_order"."user_id",
       "shop_order"."receipt"
FROM "shop_order";

SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shop_product"."id",
       "shop_product"."name",
       "shop_product"."description",
       "shop_product"."price",
       "shop_product"."discount",
       "shop_product"."created_at",
       "shop_product"."archived",
       "shop_product"."preview"
FROM "shop_product"
         INNER JOIN "shop_order_products" ON ("shop_product"."id" = "shop_order_products"."product_id")
WHERE "shop_order_products"."order_id" = 1
ORDER BY "shop_product"."name" ASC, "shop_product"."price" ASC;

SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shop_product"."id",
       "shop_product"."name",
       "shop_product"."description",
       "shop_product"."price",
       "shop_product"."discount",
       "shop_product"."created_at",
       "shop_product"."archived",
       "shop_product"."preview"
FROM "shop_product"
         INNER JOIN "shop_order_products" ON ("shop_product"."id" = "shop_order_products"."product_id")
WHERE "shop_order_products"."order_id" = 2
ORDER BY "shop_product"."name" ASC, "shop_product"."price" ASC;

