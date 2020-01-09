--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7 (Ubuntu 10.7-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.7 (Ubuntu 10.7-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO db_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO db_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO db_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO db_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO db_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO db_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO db_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO db_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO db_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO db_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO db_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO db_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO db_user;

--
-- Name: main_comment; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_comment (
    id integer NOT NULL,
    message character varying(256) NOT NULL,
    author_id integer NOT NULL,
    post_id integer NOT NULL,
    created_at timestamp with time zone NOT NULL
);


ALTER TABLE public.main_comment OWNER TO db_user;

--
-- Name: main_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.main_comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_comment_id_seq OWNER TO db_user;

--
-- Name: main_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.main_comment_id_seq OWNED BY public.main_comment.id;


--
-- Name: main_post; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_post (
    id integer NOT NULL,
    image character varying(100) NOT NULL,
    text text NOT NULL,
    author_id integer NOT NULL,
    title character varying(64) NOT NULL,
    created_at integer NOT NULL
);


ALTER TABLE public.main_post OWNER TO db_user;

--
-- Name: main_post_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.main_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_post_id_seq OWNER TO db_user;

--
-- Name: main_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.main_post_id_seq OWNED BY public.main_post.id;


--
-- Name: main_post_tags; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_post_tags (
    id integer NOT NULL,
    post_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.main_post_tags OWNER TO db_user;

--
-- Name: main_post_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.main_post_tags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_post_tags_id_seq OWNER TO db_user;

--
-- Name: main_post_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.main_post_tags_id_seq OWNED BY public.main_post_tags.id;


--
-- Name: main_profile; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_profile (
    first_name character varying(16) NOT NULL,
    last_name character varying(32) NOT NULL,
    avatar character varying(100),
    user_id integer NOT NULL,
    wallpaper character varying(100),
    birthday date
);


ALTER TABLE public.main_profile OWNER TO db_user;

--
-- Name: main_tag; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_tag (
    id integer NOT NULL,
    title character varying(16) NOT NULL
);


ALTER TABLE public.main_tag OWNER TO db_user;

--
-- Name: main_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.main_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_tag_id_seq OWNER TO db_user;

--
-- Name: main_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.main_tag_id_seq OWNED BY public.main_tag.id;


--
-- Name: main_user; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    email character varying(254) NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL
);


ALTER TABLE public.main_user OWNER TO db_user;

--
-- Name: main_user_groups; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.main_user_groups OWNER TO db_user;

--
-- Name: main_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.main_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_user_groups_id_seq OWNER TO db_user;

--
-- Name: main_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.main_user_groups_id_seq OWNED BY public.main_user_groups.id;


--
-- Name: main_user_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.main_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_user_id_seq OWNER TO db_user;

--
-- Name: main_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.main_user_id_seq OWNED BY public.main_user.id;


--
-- Name: main_user_user_permissions; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.main_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.main_user_user_permissions OWNER TO db_user;

--
-- Name: main_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.main_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.main_user_user_permissions_id_seq OWNER TO db_user;

--
-- Name: main_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.main_user_user_permissions_id_seq OWNED BY public.main_user_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: main_comment id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_comment ALTER COLUMN id SET DEFAULT nextval('public.main_comment_id_seq'::regclass);


--
-- Name: main_post id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_post ALTER COLUMN id SET DEFAULT nextval('public.main_post_id_seq'::regclass);


--
-- Name: main_post_tags id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_post_tags ALTER COLUMN id SET DEFAULT nextval('public.main_post_tags_id_seq'::regclass);


--
-- Name: main_tag id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_tag ALTER COLUMN id SET DEFAULT nextval('public.main_tag_id_seq'::regclass);


--
-- Name: main_user id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user ALTER COLUMN id SET DEFAULT nextval('public.main_user_id_seq'::regclass);


--
-- Name: main_user_groups id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_groups ALTER COLUMN id SET DEFAULT nextval('public.main_user_groups_id_seq'::regclass);


--
-- Name: main_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.main_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add comment	7	add_comment
26	Can change comment	7	change_comment
27	Can delete comment	7	delete_comment
28	Can view comment	7	view_comment
29	Can add post	8	add_post
30	Can change post	8	change_post
31	Can delete post	8	delete_post
32	Can view post	8	view_post
33	Can add profile	9	add_profile
34	Can change profile	9	change_profile
35	Can delete profile	9	delete_profile
36	Can view profile	9	view_profile
37	Can add tag	10	add_tag
38	Can change tag	10	change_tag
39	Can delete tag	10	delete_tag
40	Can view tag	10	view_tag
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	main	user
7	main	comment
8	main	post
9	main	profile
10	main	tag
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-03-23 09:33:57.203242+00
2	contenttypes	0002_remove_content_type_name	2019-03-23 09:33:57.218934+00
3	auth	0001_initial	2019-03-23 09:33:57.367311+00
4	auth	0002_alter_permission_name_max_length	2019-03-23 09:33:57.377265+00
5	auth	0003_alter_user_email_max_length	2019-03-23 09:33:57.383724+00
6	auth	0004_alter_user_username_opts	2019-03-23 09:33:57.390194+00
7	auth	0005_alter_user_last_login_null	2019-03-23 09:33:57.396296+00
8	auth	0006_require_contenttypes_0002	2019-03-23 09:33:57.399303+00
9	auth	0007_alter_validators_add_error_messages	2019-03-23 09:33:57.410023+00
10	auth	0008_alter_user_username_max_length	2019-03-23 09:33:57.430947+00
11	auth	0009_alter_user_last_name_max_length	2019-03-23 09:33:57.437174+00
12	main	0001_initial	2019-03-23 09:33:57.737767+00
13	admin	0001_initial	2019-03-23 09:33:57.799368+00
14	admin	0002_logentry_remove_auto_add	2019-03-23 09:33:57.814251+00
15	admin	0003_logentry_add_action_flag_choices	2019-03-23 09:33:57.823557+00
16	sessions	0001_initial	2019-03-23 09:33:57.873256+00
17	main	0002_auto_20190323_1255	2019-03-23 09:55:49.565998+00
18	main	0003_auto_20190323_1352	2019-03-23 10:52:19.545306+00
19	main	0004_post_title	2019-03-23 11:52:26.119562+00
20	main	0005_profile_wallpaper	2019-03-23 14:52:58.358088+00
21	main	0006_auto_20190323_1752	2019-03-23 14:52:58.461059+00
22	main	0007_auto_20190414_1502	2019-04-14 12:03:00.870209+00
23	main	0008_auto_20190414_1504	2019-04-14 12:04:11.819594+00
24	main	0009_profile_birthday	2019-04-15 05:58:05.810521+00
25	main	0010_comment_created_at	2019-04-15 06:59:38.513227+00
26	main	0011_auto_20190415_1051	2019-04-15 07:51:54.60941+00
27	main	0012_auto_20190416_0831	2019-04-16 05:34:03.935203+00
28	main	0013_auto_20190416_0832	2019-04-16 05:34:03.951604+00
29	main	0014_auto_20190416_0832	2019-04-16 05:34:03.969754+00
30	main	0015_auto_20190416_0836	2019-04-16 05:36:38.692412+00
31	main	0016_auto_20190416_0836	2019-04-16 05:36:38.709869+00
32	main	0017_auto_20190418_1129	2019-04-18 08:29:25.986793+00
33	main	0018_auto_20190418_1130	2019-04-18 08:30:55.167282+00
34	main	0019_auto_20190418_1154	2019-04-18 08:54:18.078659+00
35	auth	0010_alter_group_name_max_length	2019-04-21 14:01:46.204639+00
36	auth	0011_update_proxy_permissions	2019-04-21 14:01:46.22552+00
37	main	0020_post_myimage	2019-04-28 10:09:15.676223+00
38	main	0021_remove_post_myimage	2019-04-28 10:29:20.610489+00
39	main	0022_post_myimage	2019-04-28 10:30:37.510845+00
40	main	0023_remove_post_myimage	2019-04-28 10:35:23.303912+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
pai3huo79zsmbzwcowlf8uh07ijoyx8v	YTM2OTg0ZjAyNTgzZTk5MzI3MjkzM2NjYTExMzhlOTQ4ZGJjMmZkNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNDE4YTRhYTgwNzEyNjZlZTgwZDE4ZDYzZjE3MTFlYzBkODUzZjliIn0=	2019-04-29 07:34:50.509331+00
jdvvtmpdz1c0bd86u29zmf1nwrlugfwh	ZmExOTU5OTQ3NzQ5ZjU1YjVlNDgxYTI3NGYwNmRmNDI1NjZlNGEyYjp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjk5NTg3NzgwMWNjZDhmMmIwNjc0OTZiMTliODIzNmY0ODU5MDBhMiJ9	2019-05-02 09:37:33.136116+00
u0sy197afij62evlp5kpiqeek63hc6iu	YTM2OTg0ZjAyNTgzZTk5MzI3MjkzM2NjYTExMzhlOTQ4ZGJjMmZkNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNDE4YTRhYTgwNzEyNjZlZTgwZDE4ZDYzZjE3MTFlYzBkODUzZjliIn0=	2019-05-04 16:22:36.840953+00
hw9vwmiufaceazjj4m0h7ixouor7qqs4	YTM2OTg0ZjAyNTgzZTk5MzI3MjkzM2NjYTExMzhlOTQ4ZGJjMmZkNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNDE4YTRhYTgwNzEyNjZlZTgwZDE4ZDYzZjE3MTFlYzBkODUzZjliIn0=	2019-05-04 16:26:33.032603+00
8jelrrbpw0ana8kojtxv7zz0mgs3ermn	YTM2OTg0ZjAyNTgzZTk5MzI3MjkzM2NjYTExMzhlOTQ4ZGJjMmZkNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNDE4YTRhYTgwNzEyNjZlZTgwZDE4ZDYzZjE3MTFlYzBkODUzZjliIn0=	2019-05-05 12:38:45.391234+00
5lktlko9r9e0ct6oh3k4orm2t8vb1omc	Mjg3ZTRlM2QzOTViZDYwYWY0NWZmNTMyNGU1MDliZmM2NmJmOGRhZjp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlM2Q2ZGYyYmI1NDJmMTQ2NjhhNGIwNzFmMzg1OTIyYWU4OTk3MDg5In0=	2019-05-11 11:09:27.280395+00
4y5bkbduwxua8wdfts00h1rupj62olut	NWY5Njk3MGY5MjhhNGEyMzRiMGJhN2YyYjAxZDlkMGNhOTUzNzhhNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZDYzZjRkMWNmMjA1ODIyYjljOGEzNjMzYzM3MDNmZDY1MzJhODk1In0=	2019-05-12 10:10:03.287304+00
hjeddznnvbx94o1bj0ar8fyyyzsfkxcq	NWY5Njk3MGY5MjhhNGEyMzRiMGJhN2YyYjAxZDlkMGNhOTUzNzhhNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZDYzZjRkMWNmMjA1ODIyYjljOGEzNjMzYzM3MDNmZDY1MzJhODk1In0=	2019-05-22 08:40:03.958698+00
t2krggafqjoq3721srnikb8x5b72v5ql	NWY5Njk3MGY5MjhhNGEyMzRiMGJhN2YyYjAxZDlkMGNhOTUzNzhhNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZDYzZjRkMWNmMjA1ODIyYjljOGEzNjMzYzM3MDNmZDY1MzJhODk1In0=	2019-05-22 11:18:28.745721+00
\.


--
-- Data for Name: main_comment; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_comment (id, message, author_id, post_id, created_at) FROM stdin;
2	Питон - круто	5	9	2019-04-16 05:50:05.250796+00
3	Очень даже неплохо	5	8	2019-04-16 05:50:23.293687+00
5	Люблю js	5	6	2019-04-16 05:50:48.61422+00
6	Flask <3	5	7	2019-04-16 05:51:05.139428+00
7	Microsoft - красавчики	5	5	2019-04-16 05:51:28.477467+00
8	Корутины вперед!	3	9	2019-04-16 05:52:12.988295+00
9	Django - старик так-то	3	8	2019-04-16 05:52:40.809777+00
10	Еееееееее интерпрайз	3	4	2019-04-16 05:53:00.241059+00
11	Ох уж эти ваши джеэсы	3	6	2019-04-16 05:53:24.375797+00
12	Просто и со вкусом	3	7	2019-04-16 05:53:36.338985+00
15	React лучше	4	8	2019-04-16 05:54:44.924329+00
16	Java лучше	4	4	2019-04-16 05:55:19.034979+00
17	TypeScript лучше	4	6	2019-04-16 05:55:41.732949+00
18	Express лучше	4	7	2019-04-16 05:56:05.48892+00
19	JVM лучше	4	5	2019-04-16 05:56:21.738308+00
20	Асинхронность = сложно	6	9	2019-04-16 05:56:52.313264+00
21	Джанга еще жива!	6	8	2019-04-16 05:57:16.552526+00
22	Уже хочу попробовать	6	4	2019-04-16 05:57:33.907191+00
25	В подпункте "Кросплатформенность" очень кстати было бы теперь упомянуть и .NET Core.	6	5	2019-04-16 05:59:00.87184+00
26	Наконец-то питон стал асинхронным!	7	9	2019-04-16 05:59:39.474047+00
28	Надеюсь у майков все получится с опенсорсом	7	4	2019-04-16 06:00:12.568554+00
29	Не люблю js но куда щас без него	7	6	2019-04-16 06:00:35.004771+00
30	Будет полезно для новичков	7	7	2019-04-16 06:00:49.136918+00
31	Иногда мне кажется что статическая типизация круче динамики, но потом я вспоминаю про python.	7	5	2019-04-16 06:01:30.738616+00
\.


--
-- Data for Name: main_post; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_post (id, image, text, author_id, title, created_at) FROM stdin;
6	main/post/image/1093a00b23394ea8b7a857093556a7a3.jpg	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	6	Введение в JavaScript	1555393601
7	main/post/image/f8d461aadd2647f7919090e3f78610a3.png	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	6	Пример простого API (Flask, vue.js)	1555393646
4	main/post/image/5b904c91e6a9454b8c320c12222dda4d.png	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	5	Введение в ASP.NET Core	1555393497
8	main/post/image/11630da458e34e2fb8f72a440b3aa721.png	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	7	Быстрое и модное API (django, react.js)	1555393699
5	main/post/image/f9d619ff113a4f478eacba17c3d4605f.png	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	3	Язык C# и платформа .NET	1555393562
9	main/post/image/2c1aeeced065485e8c09cfc29cfb31f8.png	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \r\n\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	4	Будущее за asyncio	1555393740
\.


--
-- Data for Name: main_post_tags; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_post_tags (id, post_id, tag_id) FROM stdin;
6	4	9
7	4	4
8	4	6
9	5	9
11	6	2
12	7	8
13	7	1
14	7	2
15	8	3
17	9	1
18	8	2
19	7	7
\.


--
-- Data for Name: main_profile; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_profile (first_name, last_name, avatar, user_id, wallpaper, birthday) FROM stdin;
Максим	Афанасьев	main/profile/avatar/88e3758cf2ba44c891edda7332708ef7.jpeg	4	main/profile/wallpaper/104599aaf5d742e3877d9383e2e6b69b.jpg	2019-04-16
Аркадий	Рогов	main/profile/avatar/3404251a9a424edda5097240582ed73c.jpeg	5	main/profile/wallpaper/7d0c2c4ec17549a2a012bd957c6e0e04.jpg	2019-04-16
Олег	Никифоров	main/profile/avatar/f10e96985db540d48ce43f834e648c9b.jpeg	6	main/profile/wallpaper/ef53ff9483e34fe28b8025840b0d9b99.jpg	2019-04-15
Ростислав	Лаврентьев	main/profile/avatar/3e1c53f9834b4d0996c92928b612f27f.jpeg	7	main/profile/wallpaper/9e41a4fa2e0a44e7bf728c2bf9aa8a46.jpg	2019-04-16
Никита	Зуев	main/profile/avatar/a26c95347c6e408db536288f92f7ec30.jpeg	11	main/profile/wallpaper/d409fe3f40144eb7ad86e29683554c21.jpg	2019-04-17
Вячеслав	Егоров	main/profile/avatar/9b20df41c348434ea56ada536f159a76.jpeg	3	main/profile/wallpaper/dd0512ae7fac41b99e8a04ca036af4ad.jpg	2019-04-15
\.


--
-- Data for Name: main_tag; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_tag (id, title) FROM stdin;
1	python
2	javascript
3	django
4	asp .net
6	.net core
7	vue.js
8	flask
9	c#
\.


--
-- Data for Name: main_user; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_user (id, password, last_login, is_superuser, email, is_active, is_staff) FROM stdin;
7	pbkdf2_sha256$120000$pTtAExsW26vk$QqQ6EFdPcbVO0jYM6RT3maIyr8WkUuhrOOIHIm6NXpE=	\N	f	thispersondoesnotexist5@mail.ru	t	f
11	pbkdf2_sha256$120000$gW6EuibsPHOR$FmeSYT+C4EH5YeWF5ss6g0nGlUoc+5VXtOH/1h34Thc=	2019-04-18 09:37:33.130763+00	f	thispersondoesnotexist6@mail.ru	t	f
6	pbkdf2_sha256$120000$fcNAmUN3rnuJ$nG/k64oivY9QphxLmKgGC5jUm27Rb6NX5c4vglcdy6I=	2019-04-21 09:56:53.818824+00	f	thispersondoesnotexist4@mail.ru	t	f
3	pbkdf2_sha256$150000$gzIQ1CIXf2f1$GPZVgnpyZxhNYOvw5EaKEdoV+98GXi3+nZM0zQn855Y=	2019-05-08 08:37:55.438326+00	f	thispersondoesnotexist1@mail.ru	t	f
4	pbkdf2_sha256$150000$DVjpavHJi8st$FGLXWFTufnaWnAxaMp3K7ap+NQIbBLmcmTXL//49uKM=	2019-05-08 10:58:27.17406+00	f	thispersondoesnotexist2@mail.ru	t	f
5	pbkdf2_sha256$150000$DBcXNGp6vG82$RP+Vi4O2TrJ3s90Cd8bC0iC3GdE+YmkBbqR86HJRTxc=	2019-05-08 10:58:58.013016+00	f	thispersondoesnotexist3@mail.ru	t	f
1	pbkdf2_sha256$150000$7r8jTZcXXx9D$QMt2OVhKQ7ufOA8FXpLzYCyS+x5c2RT+0LI3NjfMF2k=	2019-05-08 11:18:28.743362+00	t	blogadmin@mail.ru	t	t
\.


--
-- Data for Name: main_user_groups; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: main_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.main_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 168, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 40, true);


--
-- Name: main_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.main_comment_id_seq', 62, true);


--
-- Name: main_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.main_post_id_seq', 23, true);


--
-- Name: main_post_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.main_post_tags_id_seq', 40, true);


--
-- Name: main_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.main_tag_id_seq', 9, true);


--
-- Name: main_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.main_user_groups_id_seq', 1, false);


--
-- Name: main_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.main_user_id_seq', 11, true);


--
-- Name: main_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.main_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: main_comment main_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_comment
    ADD CONSTRAINT main_comment_pkey PRIMARY KEY (id);


--
-- Name: main_post main_post_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_post
    ADD CONSTRAINT main_post_pkey PRIMARY KEY (id);


--
-- Name: main_post_tags main_post_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_post_tags
    ADD CONSTRAINT main_post_tags_pkey PRIMARY KEY (id);


--
-- Name: main_post_tags main_post_tags_post_id_tag_id_2698eb4f_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_post_tags
    ADD CONSTRAINT main_post_tags_post_id_tag_id_2698eb4f_uniq UNIQUE (post_id, tag_id);


--
-- Name: main_profile main_profile_user_id_b40d720a_pk; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_profile
    ADD CONSTRAINT main_profile_user_id_b40d720a_pk PRIMARY KEY (user_id);


--
-- Name: main_tag main_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_tag
    ADD CONSTRAINT main_tag_pkey PRIMARY KEY (id);


--
-- Name: main_tag main_tag_title_6daaa0fa_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_tag
    ADD CONSTRAINT main_tag_title_6daaa0fa_uniq UNIQUE (title);


--
-- Name: main_user main_user_email_key; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user
    ADD CONSTRAINT main_user_email_key UNIQUE (email);


--
-- Name: main_user_groups main_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_groups
    ADD CONSTRAINT main_user_groups_pkey PRIMARY KEY (id);


--
-- Name: main_user_groups main_user_groups_user_id_group_id_ae195797_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_groups
    ADD CONSTRAINT main_user_groups_user_id_group_id_ae195797_uniq UNIQUE (user_id, group_id);


--
-- Name: main_user main_user_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user
    ADD CONSTRAINT main_user_pkey PRIMARY KEY (id);


--
-- Name: main_user_user_permissions main_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_user_permissions
    ADD CONSTRAINT main_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: main_user_user_permissions main_user_user_permissions_user_id_permission_id_96b9fadf_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_user_permissions
    ADD CONSTRAINT main_user_user_permissions_user_id_permission_id_96b9fadf_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: main_comment_author_id_c7372add; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_comment_author_id_c7372add ON public.main_comment USING btree (author_id);


--
-- Name: main_comment_post_id_8158f528; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_comment_post_id_8158f528 ON public.main_comment USING btree (post_id);


--
-- Name: main_post_author_id_b6fbb16a; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_post_author_id_b6fbb16a ON public.main_post USING btree (author_id);


--
-- Name: main_post_created_at2_077f904c; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_post_created_at2_077f904c ON public.main_post USING btree (created_at);


--
-- Name: main_post_tags_post_id_ac6b2fba; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_post_tags_post_id_ac6b2fba ON public.main_post_tags USING btree (post_id);


--
-- Name: main_post_tags_tag_id_2e693427; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_post_tags_tag_id_2e693427 ON public.main_post_tags USING btree (tag_id);


--
-- Name: main_post_title_5e807736; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_post_title_5e807736 ON public.main_post USING btree (title);


--
-- Name: main_post_title_5e807736_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_post_title_5e807736_like ON public.main_post USING btree (title varchar_pattern_ops);


--
-- Name: main_profile_first_name_8e61c136; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_profile_first_name_8e61c136 ON public.main_profile USING btree (first_name);


--
-- Name: main_profile_first_name_8e61c136_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_profile_first_name_8e61c136_like ON public.main_profile USING btree (first_name varchar_pattern_ops);


--
-- Name: main_profile_last_name_70683eab; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_profile_last_name_70683eab ON public.main_profile USING btree (last_name);


--
-- Name: main_profile_last_name_70683eab_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_profile_last_name_70683eab_like ON public.main_profile USING btree (last_name varchar_pattern_ops);


--
-- Name: main_tag_title_6daaa0fa_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_tag_title_6daaa0fa_like ON public.main_tag USING btree (title varchar_pattern_ops);


--
-- Name: main_user_email_2597293b_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_user_email_2597293b_like ON public.main_user USING btree (email varchar_pattern_ops);


--
-- Name: main_user_groups_group_id_a337ba62; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_user_groups_group_id_a337ba62 ON public.main_user_groups USING btree (group_id);


--
-- Name: main_user_groups_user_id_df502602; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_user_groups_user_id_df502602 ON public.main_user_groups USING btree (user_id);


--
-- Name: main_user_user_permissions_permission_id_cd2b56a3; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_user_user_permissions_permission_id_cd2b56a3 ON public.main_user_user_permissions USING btree (permission_id);


--
-- Name: main_user_user_permissions_user_id_451ce57f; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX main_user_user_permissions_user_id_451ce57f ON public.main_user_user_permissions USING btree (user_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_main_user_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_main_user_id FOREIGN KEY (user_id) REFERENCES public.main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_comment main_comment_post_id_8158f528_fk_main_post_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_comment
    ADD CONSTRAINT main_comment_post_id_8158f528_fk_main_post_id FOREIGN KEY (post_id) REFERENCES public.main_post(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_post_tags main_post_tags_post_id_ac6b2fba_fk_main_post_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_post_tags
    ADD CONSTRAINT main_post_tags_post_id_ac6b2fba_fk_main_post_id FOREIGN KEY (post_id) REFERENCES public.main_post(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_post_tags main_post_tags_tag_id_2e693427_fk_main_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_post_tags
    ADD CONSTRAINT main_post_tags_tag_id_2e693427_fk_main_tag_id FOREIGN KEY (tag_id) REFERENCES public.main_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_profile main_profile_user_id_b40d720a_fk_main_user_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_profile
    ADD CONSTRAINT main_profile_user_id_b40d720a_fk_main_user_id FOREIGN KEY (user_id) REFERENCES public.main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_user_groups main_user_groups_group_id_a337ba62_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_groups
    ADD CONSTRAINT main_user_groups_group_id_a337ba62_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_user_groups main_user_groups_user_id_df502602_fk_main_user_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_groups
    ADD CONSTRAINT main_user_groups_user_id_df502602_fk_main_user_id FOREIGN KEY (user_id) REFERENCES public.main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_user_user_permissions main_user_user_permi_permission_id_cd2b56a3_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_user_permissions
    ADD CONSTRAINT main_user_user_permi_permission_id_cd2b56a3_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_user_user_permissions main_user_user_permissions_user_id_451ce57f_fk_main_user_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.main_user_user_permissions
    ADD CONSTRAINT main_user_user_permissions_user_id_451ce57f_fk_main_user_id FOREIGN KEY (user_id) REFERENCES public.main_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

