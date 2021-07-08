/**
 * IBM Confidential
 * OCO Source Materials
 * 5737-I23
 * Copyright IBM Corp. 2019-2020
 * The source code for this program is not published or otherwise
 * divested of its trade secrets, irrespective of what has
 * been deposited with the U.S Copyright Office.
 */
package com.ibm.automation.ops.client.model;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonToken;
import com.google.gson.stream.JsonWriter;

import java.io.IOException;
import java.math.BigDecimal;
import java.math.BigInteger;

public class AnySerializer extends TypeAdapter<AnyOfintegernumberstringboolean> {
    @Override
    public void write(JsonWriter out, AnyOfintegernumberstringboolean user) throws IOException {
        Object obj = user.getValue();

        if (obj instanceof Integer) {
            out.value(((Integer) obj).intValue());
        } else if (obj instanceof Short) {
            out.value(((Short) obj).shortValue());
        } else if (obj instanceof Byte) {
            out.value(((Byte) obj).byteValue());
        } else if (obj instanceof BigDecimal) {
            out.value(((BigDecimal) obj).doubleValue());
        } else if (obj instanceof BigInteger) {
            out.value(((BigInteger) obj).longValue());
        } else if (obj instanceof Double) {
            out.value(((Double) obj).doubleValue());
        } else if (obj instanceof Float) {
            out.value(((Float) obj).floatValue());
        } else if (obj instanceof Long) {
            out.value(((Long) obj).longValue());
        } else if (obj instanceof Boolean) {
            out.value(((Boolean) obj).booleanValue());
        } else {
            out.value(user.toString());
        }
    }

    @Override
    public AnyOfintegernumberstringboolean read(JsonReader in) throws IOException {
        AnyOfintegernumberstringboolean result = null;

        JsonToken nextToken = in.peek();
        switch (nextToken) {
            case NUMBER:


                String value = in.nextString();
                ObjectMapper mapper = new ObjectMapper();
                Number number = mapper.readValue(value, Number.class);

                result = AnyOfintegernumberstringboolean.build(number);

                break;

            case STRING:
                result = new AnyOfintegernumberstringboolean(in.nextString());
                break;
            case BOOLEAN:
                result = new AnyOfintegernumberstringboolean(in.nextBoolean());
        }

        return result;
    }
}



