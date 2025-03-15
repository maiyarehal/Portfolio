--
-- PostgreSQL database dump
--

-- Dumped from database version 12.20 (Ubuntu 12.20-1.pgdg20.04+1)
-- Dumped by pg_dump version 12.20 (Ubuntu 12.20-1.pgdg20.04+1)

-- Started on 2024-10-31 10:42:25 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 32769)
-- Name: basket_a; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.basket_a (
    a integer NOT NULL,
    fruit_a character varying(100) NOT NULL
);


ALTER TABLE public.basket_a OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 32774)
-- Name: basket_b; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.basket_b (
    b integer NOT NULL,
    fruit_b character varying(100) NOT NULL
);


ALTER TABLE public.basket_b OWNER TO postgres;

--
-- TOC entry 2962 (class 0 OID 32769)
-- Dependencies: 202
-- Data for Name: basket_a; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.basket_a (a, fruit_a) FROM stdin;
1	Apple
2	Orange
3	Banana
4	Cucumber
5	Cherry
\.


--
-- TOC entry 2963 (class 0 OID 32774)
-- Dependencies: 203
-- Data for Name: basket_b; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.basket_b (b, fruit_b) FROM stdin;
1	Orange
2	Apple
3	Watermelon
4	Pear
\.


--
-- TOC entry 2833 (class 2606 OID 32773)
-- Name: basket_a basket_a_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.basket_a
    ADD CONSTRAINT basket_a_pkey PRIMARY KEY (a);


--
-- TOC entry 2835 (class 2606 OID 32778)
-- Name: basket_b basket_b_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.basket_b
    ADD CONSTRAINT basket_b_pkey PRIMARY KEY (b);


-- Completed on 2024-10-31 10:42:25 EDT

--
-- PostgreSQL database dump complete
--
