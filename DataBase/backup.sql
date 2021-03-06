PGDMP         (                x        	   specPower "   10.13 (Ubuntu 10.13-1.pgdg18.04+1)     12.3 (Ubuntu 12.3-1.pgdg18.04+1) '    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    44492 	   specPower    DATABASE     }   CREATE DATABASE "specPower" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'es_MX.UTF-8' LC_CTYPE = 'es_MX.UTF-8';
    DROP DATABASE "specPower";
                postgres    false            �            1259    44518    dimms    TABLE     a   CREATE TABLE public.dimms (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);
    DROP TABLE public.dimms;
       public            postgres    false            �            1259    44516    dimms_id_seq    SEQUENCE     �   CREATE SEQUENCE public.dimms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.dimms_id_seq;
       public          postgres    false    201            �           0    0    dimms_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.dimms_id_seq OWNED BY public.dimms.id;
          public          postgres    false    200            �            1259    45527    form_factor    TABLE     f   CREATE TABLE public.form_factor (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.form_factor;
       public            postgres    false            �            1259    45525    form_factor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.form_factor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.form_factor_id_seq;
       public          postgres    false    205            �           0    0    form_factor_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.form_factor_id_seq OWNED BY public.form_factor.id;
          public          postgres    false    204            �            1259    44495    hardware_vendor    TABLE     k   CREATE TABLE public.hardware_vendor (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);
 #   DROP TABLE public.hardware_vendor;
       public            postgres    false            �            1259    44493    hardware_vendor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.hardware_vendor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.hardware_vendor_id_seq;
       public          postgres    false    197            �           0    0    hardware_vendor_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.hardware_vendor_id_seq OWNED BY public.hardware_vendor.id;
          public          postgres    false    196            �            1259    44526    power_supply_details    TABLE     k   CREATE TABLE public.power_supply_details (
    id integer NOT NULL,
    name character varying NOT NULL
);
 (   DROP TABLE public.power_supply_details;
       public            postgres    false            �            1259    44524    power_supply_details_id_seq    SEQUENCE     �   CREATE SEQUENCE public.power_supply_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.power_supply_details_id_seq;
       public          postgres    false    203            �           0    0    power_supply_details_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.power_supply_details_id_seq OWNED BY public.power_supply_details.id;
          public          postgres    false    202            �            1259    44506 	   processor    TABLE     e   CREATE TABLE public.processor (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);
    DROP TABLE public.processor;
       public            postgres    false            �            1259    44504    processor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.processor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.processor_id_seq;
       public          postgres    false    199            �           0    0    processor_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.processor_id_seq OWNED BY public.processor.id;
          public          postgres    false    198            %           2604    44521    dimms id    DEFAULT     d   ALTER TABLE ONLY public.dimms ALTER COLUMN id SET DEFAULT nextval('public.dimms_id_seq'::regclass);
 7   ALTER TABLE public.dimms ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            '           2604    45530    form_factor id    DEFAULT     p   ALTER TABLE ONLY public.form_factor ALTER COLUMN id SET DEFAULT nextval('public.form_factor_id_seq'::regclass);
 =   ALTER TABLE public.form_factor ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            #           2604    44498    hardware_vendor id    DEFAULT     x   ALTER TABLE ONLY public.hardware_vendor ALTER COLUMN id SET DEFAULT nextval('public.hardware_vendor_id_seq'::regclass);
 A   ALTER TABLE public.hardware_vendor ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    197    196    197            &           2604    44529    power_supply_details id    DEFAULT     �   ALTER TABLE ONLY public.power_supply_details ALTER COLUMN id SET DEFAULT nextval('public.power_supply_details_id_seq'::regclass);
 F   ALTER TABLE public.power_supply_details ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            $           2604    44509    processor id    DEFAULT     l   ALTER TABLE ONLY public.processor ALTER COLUMN id SET DEFAULT nextval('public.processor_id_seq'::regclass);
 ;   ALTER TABLE public.processor ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    199    198    199            �          0    44518    dimms 
   TABLE DATA           )   COPY public.dimms (id, name) FROM stdin;
    public          postgres    false    201   �(       �          0    45527    form_factor 
   TABLE DATA           /   COPY public.form_factor (id, name) FROM stdin;
    public          postgres    false    205   �(       �          0    44495    hardware_vendor 
   TABLE DATA           3   COPY public.hardware_vendor (id, name) FROM stdin;
    public          postgres    false    197   �(       �          0    44526    power_supply_details 
   TABLE DATA           8   COPY public.power_supply_details (id, name) FROM stdin;
    public          postgres    false    203   )       �          0    44506 	   processor 
   TABLE DATA           -   COPY public.processor (id, name) FROM stdin;
    public          postgres    false    199   -)       �           0    0    dimms_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.dimms_id_seq', 1, false);
          public          postgres    false    200            �           0    0    form_factor_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.form_factor_id_seq', 1, false);
          public          postgres    false    204            �           0    0    hardware_vendor_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.hardware_vendor_id_seq', 1, false);
          public          postgres    false    196            �           0    0    power_supply_details_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.power_supply_details_id_seq', 1, false);
          public          postgres    false    202            �           0    0    processor_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.processor_id_seq', 1, false);
          public          postgres    false    198            -           2606    44523    dimms dimms_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.dimms
    ADD CONSTRAINT dimms_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.dimms DROP CONSTRAINT dimms_pkey;
       public            postgres    false    201            1           2606    45532    form_factor form_factor_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.form_factor
    ADD CONSTRAINT form_factor_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.form_factor DROP CONSTRAINT form_factor_pkey;
       public            postgres    false    205            )           2606    44503 $   hardware_vendor hardware_vendor_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.hardware_vendor
    ADD CONSTRAINT hardware_vendor_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.hardware_vendor DROP CONSTRAINT hardware_vendor_pkey;
       public            postgres    false    197            /           2606    44534 .   power_supply_details power_supply_details_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.power_supply_details
    ADD CONSTRAINT power_supply_details_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.power_supply_details DROP CONSTRAINT power_supply_details_pkey;
       public            postgres    false    203            +           2606    44511    processor processor_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.processor
    ADD CONSTRAINT processor_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.processor DROP CONSTRAINT processor_pkey;
       public            postgres    false    199            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     